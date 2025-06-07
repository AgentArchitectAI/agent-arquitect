import json

def main(context):
    try:
        context.log(" Función iniciada")

        body_raw = context.req.body or ""
        context.log(f" Cuerpo bruto recibido: {body_raw}")

        data = json.loads(body_raw)
        prompt = data.get("prompt", "")
        context.log(f" Prompt extraído: {prompt}")

        response = {
            "status": 200,
            "output": f" Recibido correctamente el prompt: {prompt}"
        }

        context.log(f" Respuesta enviada: {response}")
        return context.res.json(response)

    except Exception as e:
        error_msg = str(e)
        context.log(f" Error al procesar: {error_msg}")
        return context.res.json({
            "status": 500,
            "error": error_msg
        }, 500)
