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
