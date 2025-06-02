import os
import logging
import json

from general import AuthTools
from aimz.tools import AimzDocumentStoreTools

log = logging.getLogger(__name__)


def GetInvoices() -> list[dict]:
    AuthTools.LoadEnviromentVariables()
    host = os.getenv('HOST')
    tenantId = os.getenv('TENANT')
    projectId = os.getenv('PROJECT_ID')
    index = 0
    limit = 200
    invoices: list[dict] = []
    variables = {
        'projectId': [projectId],
    }
    decodedToken: dict | None = None
    while True:
        if decodedToken is None or AuthTools.CheckIfTokenIsExpired(decodedToken):
            token, decodedToken = AuthTools.GetToken(host, tenantId)
            headers = AuthTools.GetHeaders(tenantId, token)
        newInvoices = AimzDocumentStoreTools.QueryAimzInvoices(host, headers, 
                                                               queryOffset=index, 
                                                               queryLimit=limit,
                                                               variables=variables)
        invoices += newInvoices
        index += limit
        log.info(f'Fetched {len(invoices)} invoices.')
        if len(newInvoices) < limit:
            break
    os.makedirs('temp', exist_ok=True)
    with open(f'./temp/invoices_{tenantId}.json', 'w') as f:
        f.write(json.dumps(invoices, indent=4))
    return invoices


if __name__=='__main__':
    invoices = GetInvoices()
    log.info(f'{len(invoices)} invoices fetched')