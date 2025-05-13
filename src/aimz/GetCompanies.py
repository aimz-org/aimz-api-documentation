import os
import logging
import json

from general import AuthTools
from aimz.tools import AimzDocumentStoreTools

log = logging.getLogger(__name__)


def GetCompanies() -> list[dict]:
    AuthTools.LoadEnviromentVariables()
    host = os.getenv('HOST')
    tenantId = os.getenv('TENANT')
    token = AuthTools.GetToken(host, tenantId)
    headers = AuthTools.GetHeaders(tenantId, token)
    index = 0
    limit = 200
    companies: list[dict] = []
    while True:
        newCompanies = AimzDocumentStoreTools.QueryAimzCompanies(host, headers, 
                                                                 queryOffset=index, 
                                                                 queryLimit=limit)
        companies += newCompanies
        index += limit
        log.info(f'Fetched {len(companies)} companies.')
        if len(newCompanies) < limit:
            break
    os.makedirs('temp', exist_ok=True)
    with open(f'./temp/companies_{tenantId}.json', 'w') as f:
        f.write(json.dumps(companies, indent=4))
    return companies


if __name__=='__main__':
    companies = GetCompanies()
    log.info(f'{len(companies)} companies fetched')