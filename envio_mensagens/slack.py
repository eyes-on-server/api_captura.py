import requests
import json


def slack_alerta(alerta):
    mensagem = {
        "text": f"""
            {alerta}
    """}

    chat_cliente = "https://hooks.slack.com/services/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"

    post_msg = requests.post(chat_cliente, data=json.dumps(mensagem))
    print(post_msg.status_code)
