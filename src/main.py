import json

def main(context):
    try:
        req = context.req
        res = context.res

        body = req.body
        context.log(f"[DEBUG] Tipo de body: {type(body)}")
        context.log(f"[DEBUG] Body recibido: {body}")

        try:
            data = json.loads(body) if body else {}
            context.log(f"[DEBUG] JSON decodificado: {data}")
        except json.JSONDecodeError as e:
            context.error(f"[ERROR] Falló json.loads(): {str(e)}")
            return res.json({
                "status": 400,
                "error": "El cuerpo no es un JSON válido",
                "raw": body
            }, 400)

        prompt = data.get("prompt", "")
        if not prompt:
            context.log("[WARN] Prompt está vacío o no presente")

        context.log(f"[DEBUG] Prompt recibido: {prompt}")

        return res.json({
            "status": 200,
            "output": f"Recibido correctamente el prompt: {prompt}"
        })

    except Exception as e:
        context.error(f"[FATAL] Excepción en la función: {str(e)}")
        return res.json({
            "status": 500,
            "error": str(e)
        }, 500)
