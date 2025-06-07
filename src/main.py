import json

def main(context):
    try:
        body_str = context.req.body  
        data = json.loads(body_str)  

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
