import json

def main(req, res):
    try:
        data = req.json
        prompt = data.get("prompt", "")

        result = {
            "status": 200,
            "output": f" Recibido correctamente el prompt: {prompt}"
        }

        return res.json(result)
    except Exception as e:
        return res.json({
            "status": 500,
            "error": str(e)
        }, 500)
