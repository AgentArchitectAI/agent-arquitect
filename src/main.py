import json

def main(req, res):
    try:
        prompt = req.json.get("prompt", "")
        return res.json({
            "status": 200,
            "output": f" Recibido correctamente el prompt: {prompt}"
        })
    except Exception as e:
        return res.json({
            "status": 500,
            "error": str(e)
        }, 500)
