import os
import sys
import base64
import ezdxf


def generar_dxf_simulado(prompt: str, codigo: str):
    contenido = f"[Plano generado para]: {prompt}"

    os.makedirs("outputs", exist_ok=True)

    filename = f"plan-{codigo}.dxf"
    path = os.path.join("outputs", filename)

    doc = ezdxf.new(dxfversion="R2010")
    msp = doc.modelspace()
    msp.add_text(contenido, dxfattribs={"height": 0.5}).set_placement((0, 0))
    doc.saveas(path)

    print(f" Archivo DXF generado: {path}")

    with open(path, "rb") as f:
        base64_dxf = base64.b64encode(f.read()).decode("utf-8")
        print(f" Base64 (primeros 100 caracteres):\n{base64_dxf[:100]}...")

    return path


def main():
    if len(sys.argv) < 3:
        print(" Uso: python test_local.py \"<prompt>\" <codigo>")
        print("Ejemplo: python test_local.py \"Casa de 2 pisos con terraza\" 123ABC")
        return

    prompt = sys.argv[1]
    codigo = sys.argv[2]
    generar_dxf_simulado(prompt, codigo)


if __name__ == "__main__":
    main()
