import json

def main(context):
    try:
        req = context.req
        res = context.res

        raw_body = req.body or req.body_raw.decode()

        print("Raw body recibido:", raw_body)

        data = json.loads(raw_body) if raw_body else {}
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
