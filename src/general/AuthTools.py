import json
import os
import logging
import time
from typing import Optional

import requests
from DockerBuildSystem import TerminalTools

from general import Tools

log = logging.getLogger(__name__)


def CheckIfTokenIsExpired(decodedToken: dict, minSecondsLeft: int = 60) -> bool:
    expiry = decodedToken['exp']
    diff = expiry - time.time()
    expired = diff <= minSecondsLeft
    return expired


def GetToken(host: str,
             tenantId: str,
             username: Optional[str] = None,
             password: Optional[str] = None) -> tuple[str, dict]:
    username = username if username is not None else os.getenv('CLIENT_USERNAME', 'client-user')
    password = password if password is not None else os.getenv('CLIENT_PASSWORD', 'client-secret')

    url: str = f"{host}/graphql"
    payload = {
        "query": """
                query authorization($username: String, $password: String) {
                    authorization(username: $username, password: $password) {
                        user {
                            token
                            decodedToken
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
    decodedToken = json.loads(response["data"]["authorization"]["user"]["decodedToken"])
    return token, decodedToken


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