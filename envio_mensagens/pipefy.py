import os
import requests
from dotenv import load_dotenv
from dao.alertas_dao import inserir_alerta

load_dotenv()

token = os.environ.get('TOKEN_PIPEFY')
id_pipe = os.environ.get('ID_PIPE')

url = "https://api.pipefy.com/graphql"


def enviar_mensagem(titulo, tipo, mensagem, momento, id_server, fk_componente):

    print('entrei no envio de mensagens!')

    body = {"query": "mutation"
                     "{ "
                        "createCard( input: "
                        "{ "
                            "pipe_id: " + id_pipe + ", "
                            "title: \"Alerta\", "
                            "fields_attributes: "
                                "["
                                    "{"
                                        "field_id: \"t_tulo_do_alerta\", "
                                        "field_value: \"" + titulo + "\""
                                    "}"
                                    "{"
                                        "field_id: \"tipo\", "
                                        "field_value: \"" + tipo + "\""
                                    "}"
                                    "{"
                                        "field_id: \"mensagem\", "
                                        "field_value: \"" + mensagem + "\""
                                    "}"
                                "]"
                        "}) "
                        "{"
                            "card "
                                "{"
                                    "title"
                                "} "
                        "}"
                     "}"
            }

    headers = {
        "authorization": token,
        "content-type": "application/json"
    }

    response = requests.post(url, headers=headers, json=body)

    print(response.text)

    inserir_alerta(3, id_server, fk_componente, titulo, mensagem, momento, tipo)
