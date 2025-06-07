import json

def main(req):
    try:
        print("Función iniciada")
        raw = req.req or ""
        print("Cuerpo crudo:", raw)
        data = json.loads(raw)
        prompt = data.get("prompt", "")
        print("Prompt recibido:", prompt)
        return {
            'json': {
                "status": 200,
                "output": f"Recibido correctamente el prompt: {prompt}"
            }
        }
    except Exception as e:
        print("Error:", str(e))
        return {
            'json': {
                "status": 500,
                "error": str(e)
            },
            'statusCode': 500
        }