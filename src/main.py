import json

def main(req, res):
    try:
        print(" Función iniciada")

        raw = req.body or ""
        print(" Cuerpo crudo:", raw)

        data = json.loads(raw)
        prompt = data.get("prompt", "")

        print(" Prompt recibido:", prompt)

        return res.json({
            "status": 200,
            "output": f" Recibido correctamente el prompt: {prompt}"
        })
    except Exception as e:
        print(" Error:", str(e))
        return res.json({
            "status": 500,
            "error": str(e)
        }, 500)
