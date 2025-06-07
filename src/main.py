import json

def main(context):
    try:
        print("Función iniciada")

        raw = context.req.payload or ""
        print("Payload crudo recibido:", raw)

        data = json.loads(raw)
        prompt = data.get("prompt", "")

        print("Prompt:", prompt)

        return context.res.json({
            "status": 200,
            "output": f"Recibido correctamente el prompt: {prompt}"
        })
    except Exception as e:
        print(" Error:", str(e))
        return context.res.json({
            "status": 500,
            "error": str(e)
        }, 500)
