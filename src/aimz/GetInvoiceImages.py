import os
import logging
import json

from general import AuthTools, Tools
from aimz.tools import AimzDocumentStoreTools
from aimz.GetInvoices import GetInvoices

log = logging.getLogger(__name__)


def GetInvoiceImages(invoices: list[dict], limit: int | None = None) -> tuple[list[dict], list[dict]]:
    AuthTools.LoadEnviromentVariables()
    host = os.getenv('HOST')
    tenantId = os.getenv('TENANT')
    invoiceImages: list[dict] = []
    storageFiles: list[dict] = []
    decodedToken: dict | None = None
    os.makedirs('temp', exist_ok=True)
    limit = limit if limit is not None else len(invoices)
    for invoice in invoices[:limit]:
        if decodedToken is None or AuthTools.CheckIfTokenIsExpired(decodedToken):
            token, decodedToken = AuthTools.GetToken(host, tenantId)
            headers = AuthTools.GetHeaders(tenantId, token)
        newInvoiceImages = AimzDocumentStoreTools.QueryExternalInvoiceImages(host, headers, 
                                                                             externalId=invoice['externalAttachmentId'],
                                                                             externalProvider=invoice['externalProvider'])
        newStorageFiles = AimzDocumentStoreTools.QueryStorageFiles(host, headers, 
                                                                   searchKey=Tools.GetStorageFileKey(Tools.GetInvoiceIdForFile(invoice), invoice['projectId']))
        invoiceImages += newInvoiceImages
        storageFiles += newStorageFiles
        with open(f'./temp/invoiceImages_{invoice["id"]}_{invoice["invoiceNumber"]}.json', 'w') as f:
            f.write(json.dumps(newInvoiceImages, indent=4))
        with open(f'./temp/storageFiles_{invoice["id"]}_{invoice["invoiceNumber"]}.json', 'w') as f:
            f.write(json.dumps(newStorageFiles, indent=4))
        log.info(f'Fetched {len(newInvoiceImages)}/{len(invoiceImages)} invoice images and {len(newStorageFiles)}/{len(storageFiles)} storage files for invoice {invoice["invoiceNumber"]}.')
    return invoiceImages, storageFiles


if __name__=='__main__':
    invoices = GetInvoices()
    invoiceImages, storageFiles = GetInvoiceImages(invoices, limit=10)
    log.info(f'{len(invoiceImages)} invoice images fetched and {len(storageFiles)} storage files fetched.')
