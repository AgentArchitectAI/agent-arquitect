import json
import ezdxf
import requests
import base64


def call_core_agent(prompt: str):
    response = requests.post(
    "http://127.0.0.1:50001/api/v1/chat", 
    json={"input": prompt},
    headers={"Content-Type": "application/json"},
    timeout=30
)


    print(f" Respuesta HTTP: {response.status_code}")
    print(f" Body: {response.text}")

    if response.status_code != 200:
        raise Exception("Error al llamar al núcleo")

    if response.text.strip().startswith("<!DOCTYPE html>"):
        raise Exception("Estás llamando al HTML del frontend, no al backend real")

    return response.json().get("output", "Diseño base de casa")


def generate_dxf(text: str, filename="plan.dxf"):
    doc = ezdxf.new(dxfversion="R2010")
    msp = doc.modelspace()
    msp.add_text(text, dxfattribs={"height": 0.5}).set_pos((0, 0), align="LEFT")
    path = f"./{filename}"
    doc.saveas(path)
    return path


def main():
    prompt = "Diseña una casa moderna de 2 pisos con terraza y cochera"
    print(f"\n Enviando prompt al agente núcleo:\n{prompt}\n")

    reply = call_core_agent(prompt)
    print(f"\n Respuesta del núcleo:\n{reply}\n")

    path = generate_dxf(reply)
    print(f" Archivo .dxf generado en: {path}")

    with open(path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
        print(f" Base64 del archivo (primeros 100 chars):\n{encoded[:100]}...")


if __name__ == "__main__":
    main()
