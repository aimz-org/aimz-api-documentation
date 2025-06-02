import json
import uuid
from python_graphql_client import GraphqlClient

from general import Tools
from aimz.tools import AimzGraphqlTools


def QueryAimzProjects(host: str, 
                      headers: dict,
                      queryOffset: int | None = None,
                      queryLimit: int | None = None, 
                      variables: dict | None = None) -> list[dict]:
    variables = variables if variables is not None else {}
    if queryOffset is not None: variables['queryOffset'] = queryOffset
    if queryLimit is not None: variables['queryLimit'] = queryLimit
    client = GraphqlClient(endpoint=f'{host}/graphql', headers=headers)
    query = AimzGraphqlTools.QUERY_AIMZ_PROJECTS
    data = client.execute(query=query, variables=variables)
    Tools.AssertGraphqlSuccess(data)
    return data['data']['projects']['documents']


def QueryAimzAccounts(host: str, 
                      headers: dict,
                      queryOffset: int | None = None,
                      queryLimit: int | None = None, 
                      variables: dict | None = None) -> list[dict]:
    variables = variables if variables is not None else {}
    if queryOffset is not None: variables['queryOffset'] = queryOffset
    if queryLimit is not None: variables['queryLimit'] = queryLimit
    client = GraphqlClient(endpoint=f'{host}/graphql', headers=headers)
    query = AimzGraphqlTools.QUERY_AIMZ_ACCOUNTS
    data = client.execute(query=query, variables=variables)
    Tools.AssertGraphqlSuccess(data)
    return data['data']['accounts']['documents']


def QueryAimzInvoices(host: str, 
                      headers: dict,
                      queryOffset: int | None = None,
                      queryLimit: int | None = None, 
                      variables: dict | None = None) -> list[dict]:
    variables = variables if variables is not None else {}
    if queryOffset is not None: variables['queryOffset'] = queryOffset
    if queryLimit is not None: variables['queryLimit'] = queryLimit
    client = GraphqlClient(endpoint=f'{host}/graphql', headers=headers)
    query = AimzGraphqlTools.QUERY_AIMZ_INVOICES
    data = client.execute(query=query, variables=variables)
    Tools.AssertGraphqlSuccess(data)
    return data['data']['invoices']['documents']


def QueryAimzCompanies(host: str, 
                       headers: dict,
                       queryOffset: int | None = None,
                       queryLimit: int | None = None, 
                       variables: dict | None = None) -> list[dict]:
    variables = variables if variables is not None else {}
    if queryOffset is not None: variables['queryOffset'] = queryOffset
    if queryLimit is not None: variables['queryLimit'] = queryLimit
    client = GraphqlClient(endpoint=f'{host}/graphql', headers=headers)
    query = AimzGraphqlTools.QUERY_AIMZ_COMPANIES
    data = client.execute(query=query, variables=variables)
    Tools.AssertGraphqlSuccess(data)
    return data['data']['companies']['documents']


def QueryAimzChangeOrders(host: str, 
                          headers: dict,
                          queryOffset: int | None = None,
                          queryLimit: int | None = None, 
                          variables: dict | None = None) -> list[dict]:
    variables = variables if variables is not None else {}
    if queryOffset is not None: variables['queryOffset'] = queryOffset
    if queryLimit is not None: variables['queryLimit'] = queryLimit
    client = GraphqlClient(endpoint=f'{host}/graphql', headers=headers)
    query = AimzGraphqlTools.QUERY_AIMZ_CHANGE_ORDERS
    data = client.execute(query=query, variables=variables)
    Tools.AssertGraphqlSuccess(data)
    return data['data']['changeOrders']['documents']


def QueryAimzContracts(host: str, 
                       headers: dict,
                       queryOffset: int | None = None,
                       queryLimit: int | None = None, 
                       variables: dict | None = None) -> list[dict]:
    variables = variables if variables is not None else {}
    if queryOffset is not None: variables['queryOffset'] = queryOffset
    if queryLimit is not None: variables['queryLimit'] = queryLimit
    client = GraphqlClient(endpoint=f'{host}/graphql', headers=headers)
    query = AimzGraphqlTools.QUERY_AIMZ_CONTRACTS
    data = client.execute(query=query, variables=variables)
    Tools.AssertGraphqlSuccess(data)
    return data['data']['contracts']['documents']


def QueryStorageFiles(host: str,
                      headers: dict,
                      queryOffset: int | None = None,
                      queryLimit: int | None = None,
                      searchKey: str | None = None,
                      id: uuid.UUID | None = None,
                      filename: str | None = None,
                      key: str | None = None,
                      changed: str | None = None,
                      changedBy: str | None = None,
                      tags: list[str] | None = None,
                      includeContent: bool | None = None) -> list[dict]:
    client = GraphqlClient(endpoint=f'{host}/graphql', headers=headers)
    query = AimzGraphqlTools.QUERY_FILE_STORE_FILES
    variables = {
        'searchIndexStart': queryOffset,
        'searchIndexStop': queryOffset + queryLimit if queryOffset is not None and queryLimit is not None else None,
        'searchKey': searchKey,
        'id': id,
        'filename': filename,
        'key': key,
        'changed': changed,
        'changedBy': changedBy,
        'tags': tags,
        'includeContent': includeContent,
    }
    data = client.execute(query=query, variables=variables)
    Tools.AssertGraphqlSuccess(data)
    return data['data']['storageFiles']


def QueryExternalInvoiceImages(host: str,
                               headers: dict,
                               externalId: str,
                               externalProvider: str,
                               settingId: str | None = None,
                               settingOverrides: list[dict] | None = None) -> list[dict]:
    if Tools.IsStringEmpty(externalId) or Tools.IsStringEmpty(externalProvider) or Tools.IsDefaultExternalProvider(externalProvider):
        return []
    client = GraphqlClient(endpoint=f'{host}/graphql', headers=headers)
    query = AimzGraphqlTools.QUERY_EXTERNAL_INVOICE_IMAGES
    variables = {
        'externalId': externalId,
        'externalProvider': externalProvider.upper(),
    }
    if settingId is not None:
        variables['settingId'] = settingId
    if settingOverrides is not None:
        variables['settingOverrides'] = json.dumps(settingOverrides)
    data = client.execute(query=query, variables=variables)
    Tools.AssertGraphqlSuccess(data)
    return data['data']['externalInvoiceImages']
