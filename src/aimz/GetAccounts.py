import os
import logging
import json

from general import AuthTools
from aimz.tools import AimzDocumentStoreTools

log = logging.getLogger(__name__)


def GetAccounts() -> list[dict]:
    AuthTools.LoadEnviromentVariables()
    host = os.getenv('HOST')
    tenantId = os.getenv('TENANT')
    projectId = os.getenv('PROJECT_ID')
    token = AuthTools.GetToken(host, tenantId)
    headers = AuthTools.GetHeaders(tenantId, token)
    index = 0
    limit = 200
    accounts: list[dict] = []
    variables = {
        'projectId': [projectId],
    }
    while True:
        newAccounts = AimzDocumentStoreTools.QueryAimzAccounts(host, headers, 
                                                               queryOffset=index, 
                                                               queryLimit=limit,
                                                               variables=variables)
        accounts += newAccounts
        index += limit
        log.info(f'Fetched {len(accounts)} accounts.')
        if len(newAccounts) < limit:
            break
    os.makedirs('temp', exist_ok=True)
    with open(f'./temp/accounts_{tenantId}.json', 'w') as f:
        f.write(json.dumps(accounts, indent=4))
    return accounts


if __name__=='__main__':
    accounts = GetAccounts()
    log.info(f'{len(accounts)} accounts fetched')