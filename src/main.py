import os
import json
import tempfile
import ezdxf

def draw_zones(msp, zonas):
    for zona in zonas:
        nombre = zona.get("nombre", "zona")
        x, y = zona.get("pos", [0, 0])
        w, h = zona.get("tam", [1000, 1000])

        msp.add_lwpolyline([
            (x, y), (x + w, y), (x + w, y + h), (x, y + h), (x, y)
        ], close=True)

        msp.add_text(nombre, dxfattribs={"height": 250}).set_pos((x + 100, y + h - 300))

def main(context):
    try:
        data = json.loads(context.req.body)  

        tipo = data.get("tipo", "espacio")
        dimensiones = data.get("dimensiones", [6000, 4000])  
        zonas = data.get("zonas", [])

        width, height = dimensiones

        doc = ezdxf.new("R2010")
        msp = doc.modelspace()

        msp.add_lwpolyline([(0, 0), (width, 0), (width, height), (0, height), (0, 0)], close=True)
        draw_zones(msp, zonas)

        with tempfile.NamedTemporaryFile(delete=False, suffix='.dxf') as tmp:
            doc.saveas(tmp.name)
            tmp.seek(0)
            dxf_bytes = tmp.read()

        os.unlink(tmp.name)

        return context.res.send(
            dxf_bytes,
            content_type='application/dxf',
            status_code=200,
            headers={'Content-Disposition': f'attachment; filename="plano_{tipo}.dxf"'}
        )

    except Exception as e:
        return context.res.json({"error": str(e)}, status_code=500)
