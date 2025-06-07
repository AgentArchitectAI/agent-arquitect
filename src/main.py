import json

def main(context):
    try:
        req = context.req
        res = context.res

        raw_body = req.body_raw.decode() if isinstance(req.body_raw, bytes) else req.body_raw
        print("Raw body recibido:", raw_body)

        data = json.loads(raw_body) if raw_body else {}
        prompt = data.get("prompt", "")
        print("Prompt recibido:", prompt)

        return res.json({
            "status": 200,
            "output": f"Recibido correctamente el prompt: {prompt}"
        })
    except Exception as e:
        print(" Error en ejecución:", str(e))
        return res.json({
            "status": 500,
            "error": str(e)
        }, 500)
