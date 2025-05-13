import os
import logging
import json

from general import AuthTools
from aimz.tools import AimzDocumentStoreTools

log = logging.getLogger(__name__)


def GetContracts() -> list[dict]:
    AuthTools.LoadEnviromentVariables()
    host = os.getenv('HOST')
    tenantId = os.getenv('TENANT')
    projectId = os.getenv('PROJECT_ID')
    token = AuthTools.GetToken(host, tenantId)
    headers = AuthTools.GetHeaders(tenantId, token)
    index = 0
    limit = 200
    contracts: list[dict] = []
    variables = {
        'projectId': [projectId],
    }
    while True:
        newContracts = AimzDocumentStoreTools.QueryAimzContracts(host, headers, 
                                                                 queryOffset=index, 
                                                                 queryLimit=limit,
                                                                 variables=variables)
        contracts += newContracts
        index += limit
        log.info(f'Fetched {len(contracts)} contracts.')
        if len(newContracts) < limit:
            break
    os.makedirs('temp', exist_ok=True)
    with open(f'./temp/contracts_{tenantId}.json', 'w') as f:
        f.write(json.dumps(contracts, indent=4))
    return contracts


if __name__=='__main__':
    contracts = GetContracts()
    log.info(f'{len(contracts)} contracts fetched')