# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
from jira import JIRA



jira_token = "ATATT3xFfGF0qQSV8Yv2KCN5uGBfxwWardioua9TlmgdJfk_lXTxmHG0HYb71Ko7ETenQKKZuYB3hU0H4ig7Ip5iTwETBdMIIuMWe2ceHZwsp7ppUFog8L0r3u64xVicfpx2aW5ekSdm-O4VHL25--Poejq5grLO0ODrshAzooMcfEuExrKtDCc=EFD8BFBC"
url = "https://eyes-on-server.atlassian.net/rest/api/3/issue"
server_name = "https://eyes-on-server.atlassian.net"
email = "eyes_on_server@outlook.com"

jira_connection = JIRA(
  basic_auth=(email, jira_token),
  server=server_name
)

def chamado(mensagem, descricao):
  issue_dict = {
    'project': {'key': 'EOS'},
    'summary': mensagem,
    'description': descricao,
    'issuetype': {'id': '10007'},
  }

  new_issue = jira_connection.create_issue(fields=issue_dict)