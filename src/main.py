import json

def main(req, res):
    try:
        raw = req.body.decode("utf-8") if isinstance(req.body, bytes) else req.body
        print(" Body recibido:", raw)

        data = json.loads(raw)
        prompt = data.get("prompt", "")

        print(" Prompt:", prompt)

        return res.json({
            "status": 200,
            "output": f"Recibido correctamente el prompt: {prompt}"
        })
    except Exception as e:
        print(" Error:", str(e))
        return res.json({
            "status": 500,
            "error": str(e)
        }, 500)
