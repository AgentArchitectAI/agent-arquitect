import json

def main(context):
    req = context.req
    res = context.res

    try:
        raw_input = json.loads(req.body)
        context.log(f"[DEBUG] Entrada cruda: {raw_input}")

        data_str = raw_input.get("data", "")
        data = json.loads(data_str)
        context.log(f"[DEBUG] JSON de 'data': {data}")

        prompt = data.get("prompt", "")
        context.log(f"[DEBUG] Prompt: {prompt}")

        return res.json({
            "ok": True,
            "prompt": prompt
        })

    except Exception as e:
        context.error(f"[ERROR]: {str(e)}")
        return res.json({ "error": str(e) }, 500)
