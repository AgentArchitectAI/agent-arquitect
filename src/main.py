import json

def main(context):
    try:
        req = context.req
        res = context.res

        body = req.body

        print("Raw body recibido:", body)

        data = json.loads(body) if body else {}
        prompt = data.get("prompt", "")
        print("Prompt recibido:", prompt)

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
