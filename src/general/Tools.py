import logging
from typing import Union
import uuid

log = logging.getLogger(__name__)

DEFAULT_EXTERNAL_PROVIDER = 'aimz'


def AssertGraphqlSuccess(data: dict) -> None:
    if "errors" in data:
        errors = data["errors"]
        errorMsg = "".join([errors[i]["message"] for i in range(len(errors)) if "message" in errors[i]])
        raise Exception(errorMsg)


def IsStringEmpty(param: Union[str, uuid.UUID, None]) -> bool:
    return param is None or len(str(param).strip()) == 0



def IsDefaultExternalProvider(externalProvider: str | None) -> bool:
    return externalProvider is None or externalProvider.strip().lower() == DEFAULT_EXTERNAL_PROVIDER


def GetInvoiceIdForFile(invoice: dict) -> str | None:
    if invoice['invoiceIsSplitManually']:
        return invoice['parentId']
    else:
        return invoice['id']


def GetStorageFileKey(documentId: str | None = None, 
                      projectId: str | None = None, 
                      fileKey: str | None = None) -> str:
    storageFileKey = 'aimz'
    if projectId:
        storageFileKey += f'_{projectId}'
    if documentId:
        storageFileKey += f'_{documentId}'
    if fileKey and len(fileKey.strip()) > 0:
        storageFileKey = f'{storageFileKey}_{fileKey}'
    return storageFileKey
