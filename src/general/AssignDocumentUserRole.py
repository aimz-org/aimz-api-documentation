import argparse
import logging
import os

from python_graphql_client import GraphqlClient

from general import AuthTools, Tools

log = logging.getLogger(__name__)

MUTATE_USER = """
mutation user($email: String, $name: String, $verifyEmail: Boolean, $clientId: String, $roles: [RoleInput], $emailRedirectUri: String) {
  mutateUser(
    email: $email
    name: $name
    verifyEmail: $verifyEmail
    clientId: $clientId
    roles: $roles
    emailRedirectUri: $emailRedirectUri
  ) {
    user {
      id
      name
      email
      emailVerified
      roles {
        id
        name
        delete
        __typename
      }
      __typename
    }
    __typename
  }
}
"""

QUERY_ROLES = """
query roles($clientId: String, $roleNames: [String]) {
  roles(clientId: $clientId, roleNames: $roleNames) {
    id
    name
    __typename
  }
}
"""

MUTATE_DOCUMENT_USER_ROLES = """
mutation mutateDocumentUserRoles($userId: String!, $documentRoles: [DocumentRoleDataInput!]!) {
  mutateDocumentUserRoles(userId: $userId, documentRoles: $documentRoles) {
    success
    __typename
  }
}
"""


def MutateUser(client: GraphqlClient, email: str, clientId: str, verifyEmail: bool, emailRedirectUri: str | None) -> dict:
    variables = {
        "clientId": clientId,
        "email": email,
        "verifyEmail": verifyEmail,
        "emailRedirectUri": emailRedirectUri,
    }
    data = client.execute(query=MUTATE_USER, variables=variables)
    Tools.AssertGraphqlSuccess(data)
    return data["data"]["mutateUser"]["user"]


def QueryRole(client: GraphqlClient, clientId: str, roleName: str) -> dict:
    variables = {
        "clientId": clientId,
        "roleNames": [roleName],
    }
    data = client.execute(query=QUERY_ROLES, variables=variables)
    Tools.AssertGraphqlSuccess(data)
    roles = data["data"]["roles"]
    if len(roles) != 1:
        raise Exception(f"Expected exactly one role named '{roleName}', got {len(roles)}.")
    return roles[0]


def MutateDocumentUserRoles(client: GraphqlClient, userId: str, documentId: str, role: str, roleId: str, delete: bool = False) -> bool:
    variables = {
        "userId": userId,
        "documentRoles": [
            {
                "documentId": documentId,
                "role": role,
                "roleId": roleId,
                "delete": delete,
            },
        ],
    }
    data = client.execute(query=MUTATE_DOCUMENT_USER_ROLES, variables=variables)
    Tools.AssertGraphqlSuccess(data)
    return data["data"]["mutateDocumentUserRoles"]["success"]


def AssignDocumentUserRole(email: str,
                           documentId: str,
                           role: str = "owner",
                           clientId: str = "aimz-aimz-client",
                           verifyEmail: bool = True,
                           emailRedirectUri: str | None = None) -> dict:
    AuthTools.LoadEnviromentVariables()
    host = os.getenv("HOST")
    tenantId = os.getenv("TENANT")
    if Tools.IsStringEmpty(host) or Tools.IsStringEmpty(tenantId):
        raise Exception("HOST and TENANT must be set in the environment or private.env.")

    token, _ = AuthTools.GetToken(host, tenantId)
    headers = AuthTools.GetHeaders(tenantId, token)
    client = GraphqlClient(endpoint=f"{host}/graphql", headers=headers)

    user = MutateUser(client, email, clientId, verifyEmail, emailRedirectUri)
    roleName = f"PROJECT-{documentId}-{role}"
    roleData = QueryRole(client, clientId, roleName)
    success = MutateDocumentUserRoles(client, user["id"], documentId, role, roleData["id"])

    return {
        "success": success,
        "user": user,
        "role": roleData,
    }


def ParseArgs() -> argparse.Namespace:
    AuthTools.LoadEnviromentVariables()
    parser = argparse.ArgumentParser(description="Create/update a user and assign a project/document role.")
    parser.add_argument("--email", default=os.getenv("USER_EMAIL"), required=os.getenv("USER_EMAIL") is None, help="User email to mutate.")
    parser.add_argument("--document-id", default=os.getenv("DOCUMENT_ID") or os.getenv("PROJECT_ID"), required=os.getenv("DOCUMENT_ID") is None and os.getenv("PROJECT_ID") is None, help="Project/document id used in the role name and role assignment.")
    parser.add_argument("--role", default=os.getenv("ROLE", "owner"), help="Role suffix to assign, for example owner.")
    parser.add_argument("--client-id", default=os.getenv("CLIENT_ID", "aimz-aimz-client"), help="Aimz client id.")
    parser.add_argument("--email-redirect-uri", default=os.getenv("EMAIL_REDIRECT_URI"), help="Redirect URI used when verify email is enabled.")
    parser.add_argument("--skip-verify-email", action="store_true", help="Do not send/trigger email verification.")
    return parser.parse_args()


if __name__ == "__main__":
    args = ParseArgs()
    result = AssignDocumentUserRole(email=args.email,
                                    documentId=args.document_id,
                                    role=args.role,
                                    clientId=args.client_id,
                                    verifyEmail=not args.skip_verify_email,
                                    emailRedirectUri=args.email_redirect_uri)
    log.info(f"Assigned role '{result['role']['name']}' to user '{result['user']['email']}'. Success: {result['success']}")
