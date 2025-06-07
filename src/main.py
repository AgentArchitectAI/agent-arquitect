import json

def main(req, res):
    try:
        data = req.json if req.json else {}
        print(" Body recibido:", data)

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
