import os
import json
import tempfile
import ezdxf
from datetime import datetime

def draw_zones(doc, msp, zonas, width, height):
    for zona in zonas:
        nombre = zona.get("nombre", "zona")
        pos = zona.get("pos")
        tam = zona.get("tam")

        if not isinstance(pos, list) or len(pos) != 2 or not isinstance(tam, list) or len(tam) != 2:
            continue

        x, y = pos
        w, h = tam

        if x < 0 or y < 0 or x + w > width or y + h > height:
            continue

        layer_name = nombre.lower().replace(" ", "_")
        if layer_name not in doc.layers:
            doc.layers.new(name=layer_name)

        msp.add_lwpolyline([
            (x, y), (x + w, y), (x + w, y + h), (x, y + h), (x, y)
        ], close=True, dxfattribs={"layer": layer_name})

        text_height = max(min(w, h) * 0.15, 200)
        msp.add_text(nombre, dxfattribs={"height": text_height, "layer": layer_name}).set_pos((x + 100, y + h - 300))

def add_metadata(msp, tipo, width, height):
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    msp.add_text(f"Plano: {tipo}", dxfattribs={"height": 250, "layer": "metadata"}).set_pos((width - 2500, height + 300))
    msp.add_text(f"Generado: {timestamp}", dxfattribs={"height": 200, "layer": "metadata"}).set_pos((width - 2500, height + 0))

def main(req, res):
    try:
        data = req.json

        if not isinstance(data, dict):
            return res.json({"error": "Input inválido"}, status_code=400)

        tipo = data.get("tipo", "espacio")
        dimensiones = data.get("dimensiones", [6000, 4000])
        zonas = data.get("zonas", [])

        if not isinstance(dimensiones, list) or len(dimensiones) != 2:
            return res.json({"error": "Dimensiones inválidas"}, status_code=400)

        width, height = dimensiones

        doc = ezdxf.new("R2010")
        msp = doc.modelspace()

        if "metadata" not in doc.layers:
            doc.layers.new(name="metadata")

        msp.add_lwpolyline([
            (0, 0), (width, 0), (width, height), (0, height), (0, 0)
        ], close=True, dxfattribs={"layer": "metadata"})

        draw_zones(doc, msp, zonas, width, height)

        add_metadata(msp, tipo, width, height)

        with tempfile.NamedTemporaryFile(delete=False, suffix='.dxf') as tmp:
            doc.saveas(tmp.name)
            tmp.seek(0)
            dxf_bytes = tmp.read()
        os.unlink(tmp.name)

        return res.send(dxf_bytes, content_type='application/dxf', status_code=200, headers={
            'Content-Disposition': f'attachment; filename="plano_{tipo}.dxf"'
        })

    except Exception as e:
        return res.json({"error": str(e)}, status_code=500)
