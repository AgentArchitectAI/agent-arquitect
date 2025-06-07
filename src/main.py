import json

def main(req, res):
    try:
        data = req.json
        prompt = data.get("prompt", "")
        return res.json({
            "message": f"✅ Recibido correctamente el prompt: {prompt}"
        })
    except Exception as e:
        return res.json({ "error": str(e) }, 500)
