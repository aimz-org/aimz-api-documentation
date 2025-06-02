import os
import logging
import json

from general import AuthTools
from aimz.tools import AimzDocumentStoreTools

log = logging.getLogger(__name__)


def GetChangeOrders() -> list[dict]:
    AuthTools.LoadEnviromentVariables()
    host = os.getenv('HOST')
    tenantId = os.getenv('TENANT')
    projectId = os.getenv('PROJECT_ID')
    index = 0
    limit = 200
    changeOrders: list[dict] = []
    variables = {
        'projectId': [projectId],
    }
    decodedToken: dict | None = None
    while True:
        if decodedToken is None or AuthTools.CheckIfTokenIsExpired(decodedToken):
            token, decodedToken = AuthTools.GetToken(host, tenantId)
            headers = AuthTools.GetHeaders(tenantId, token)
        newChangeOrders = AimzDocumentStoreTools.QueryAimzChangeOrders(host, headers, 
                                                                       queryOffset=index, 
                                                                       queryLimit=limit,
                                                                       variables=variables)
        changeOrders += newChangeOrders
        index += limit
        log.info(f'Fetched {len(changeOrders)} changeOrders.')
        if len(newChangeOrders) < limit:
            break
    os.makedirs('temp', exist_ok=True)
    with open(f'./temp/changeOrders_{tenantId}.json', 'w') as f:
        f.write(json.dumps(changeOrders, indent=4))
    return changeOrders


if __name__=='__main__':
    changeOrders = GetChangeOrders()
    log.info(f'{len(changeOrders)} changeOrders fetched')