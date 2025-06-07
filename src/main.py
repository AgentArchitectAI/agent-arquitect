import json

def main(context):
    try:
        body = context.req.body
        data = json.loads(body)
        prompt = data.get("prompt", "")

        return context.res.json({
            "status": 200,
            "output": f" Recibido correctamente el prompt: {prompt}"
        })
    except Exception as e:
        return context.res.json({
            "status": 500,
            "error": str(e)
        }, 500)

