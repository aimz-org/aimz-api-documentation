import os
import logging
from typing import Optional

import requests
from DockerBuildSystem import TerminalTools

from general import Tools

log = logging.getLogger(__name__)


def GetToken(host: str,
             tenantId: str,
             username: Optional[str] = None,
             password: Optional[str] = None) -> str:
    username = username if username is not None else os.getenv('CLIENT_USERNAME', 'client-user')
    password = password if password is not None else os.getenv('CLIENT_PASSWORD', 'client-secret')

    url: str = f"{host}/graphql"
    payload = {
        "query": """
                query authorization($username: String, $password: String) {
                    authorization(username: $username, password: $password) {
                        user {
                            token
                        }
                    }
                }
                """,
        "variables": {
            "username": username,
            "password": password,
        },
    }
    result = requests.post(url, json=payload, headers={'tenant': tenantId})
    result.raise_for_status()
    response = result.json()
    Tools.AssertGraphqlSuccess(response)
    token = response["data"]["authorization"]["user"]["token"]
    return token


def GetHeaders(tenantId: str, token: str) -> dict:
    headers = {
        "tenant": tenantId,
        "Authorization": token,
    }
    return headers


def LoadEnviromentVariables() -> None:
    envFiles = ['private.env',
                '.env']
    for envFile in envFiles:
        TerminalTools.LoadDefaultEnvironmentVariablesFile(envFile)