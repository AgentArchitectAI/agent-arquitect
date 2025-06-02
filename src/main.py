import os
import json
import ezdxf
import requests
import base64
from appwrite.client import Client
from appwrite.exception import AppwriteException

def main(context):
    try:
        body = context.req.body
        prompt = json.loads(body).get("prompt", "")

        if not prompt:
            return context.res.json({"error": "No prompt provided"}, 400)

        response = requests.post(
            "https://silver-walls-kneel.loca.lt",
            json={"input": prompt},
            headers={"Content-Type": "application/json"},
            timeout=30
        )

        if response.status_code != 200:
            return context.res.json({"error": "Failed to call core agent"}, 500)

        agent_reply = response.json().get("output", "Diseño base de casa")

        doc = ezdxf.new(dxfversion="R2010")
        msp = doc.modelspace()
        msp.add_text(agent_reply, dxfattribs={"height": 0.5}).set_pos((0, 0), align="LEFT")
        dxf_path = "/tmp/plan.dxf"
        doc.saveas(dxf_path)

        with open(dxf_path, "rb") as f:
            dxf_base64 = base64.b64encode(f.read()).decode("utf-8")

        return context.res.json({
            "status": "ok",
            "prompt_used": prompt,
            "agent_reply": agent_reply,
            "filename": "plan.dxf",
            "base64": dxf_base64
        })

    except Exception as e:
        return context.res.json({"error": str(e)}, 500)
