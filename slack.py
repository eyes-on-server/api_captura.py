import requests
import json

def slackAlerta(alerta):
    mensagem = {
        "text": f"""
            {alerta}
    """}

    chatCliente = "https://hooks.slack.com/services/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"

    postMsg = requests.post(chatCliente, data=json.dumps(mensagem))
    print(postMsg.status_code)
