import os
import logging
import json

from general import AuthTools
from aimz.tools import AimzDocumentStoreTools

log = logging.getLogger(__name__)


def GetProjects() -> list[dict]:
    AuthTools.LoadEnviromentVariables()
    host = os.getenv('HOST')
    tenantId = os.getenv('TENANT')
    token = AuthTools.GetToken(host, tenantId)
    headers = AuthTools.GetHeaders(tenantId, token)
    index = 0
    limit = 200
    projects: list[dict] = []
    while True:
        newProjects = AimzDocumentStoreTools.QueryAimzProjects(host, headers, 
                                                               queryOffset=index, 
                                                               queryLimit=limit)
        projects += newProjects
        index += limit
        log.info(f'Fetched {len(projects)} projects.')
        if len(newProjects) < limit:
            break
    os.makedirs('temp', exist_ok=True)
    with open(f'./temp/projects_{tenantId}.json', 'w') as f:
        f.write(json.dumps(projects, indent=4))
    return projects


if __name__=='__main__':
    projects = GetProjects()
    log.info(f'{len(projects)} projects fetched')