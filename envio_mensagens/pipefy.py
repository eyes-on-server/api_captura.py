import os
import requests
from dotenv import load_dotenv
from dao.alertas_dao import inserir_alerta
from dao.componente_medida_dao import consultar_componente_medida
from dao.servidor_dao import consultar_servidor
from utils.informacoes_maquina import get_mac_address

load_dotenv()

token = os.environ.get('TOKEN_PIPEFY')
id_pipe = os.environ.get('ID_PIPE')

url = "https://api.pipefy.com/graphql"


def enviar_mensagem(tipo_alerta, momento, tipo_componente_medida, valor):

    print('entrei no envio de mensagens!')

    servidor = consultar_servidor(get_mac_address())[0]

    titulo = f"Alerta {tipo_alerta} no servidor {servidor[2]}"
    mensagem = f"Detectamos que o/a {tipo_componente_medida.value['nome']} registrou um valor de {valor}, entrando assim no estado de {tipo_alerta}"

    query = f"""
    mutation {{
        createCard(input: {{
            pipe_id: "{id_pipe}",
            title: "Alerta",
            fields_attributes: [
                {{
                    field_id: "t_tulo_do_alerta",
                    field_value: "{titulo}"
                }},
                {{
                    field_id: "tipo",
                    field_value: "{tipo_alerta}"
                }},
                {{
                    field_id: "mensagem",
                    field_value: "{mensagem}"
                }}
            ]
        }}) {{
            card {{
                title
            }}
        }}
    }}
    """

    headers = {
        "authorization": token,
        "content-type": "application/json"
    }

    response = requests.post(url, headers=headers, json={"query": query})

    print(response.text)

    inserir_alerta(servidor[1], servidor[0], consultar_componente_medida(tipo_componente_medida.name)[0][0], titulo, mensagem, momento, tipo_alerta)
