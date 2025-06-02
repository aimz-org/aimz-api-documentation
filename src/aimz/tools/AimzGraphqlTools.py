QUERY_AIMZ_PROJECTS = '''
    query projects($queryOffset: Int, $queryLimit: Int) {
        projects(queryOffset: $queryOffset, queryLimit: $queryLimit) {
            count
            documents {
                id
                activeState
                documentType
                created
                name
                projectNumber
                description
                projectType
                contractModel
                projectPhase
                bidStatus
                changeOrderSetting
                accountSetting
                accrualSetting
                crewResourceSetting
                contractValue
                administrationBudget
                salaryAdjustmentDate
                salaryAdjustmentPercent
                hoursPerMonth
                externalProvider
                externalId
                projectStart
                projectEnd
                surchargePercent
                riskConsequenceLimit
                updateAccounts
                address {
                    street
                    city
                    state
                    postcode
                    country
                    coordinate {
                        latitude
                        longitude
                    }
                }
            }
        }
    }
'''

QUERY_AIMZ_ACCOUNTS = '''
    query accounts($queryOffset: Int, $queryLimit: Int, $projectId: [String]) {
        accounts(
            queryOffset: $queryOffset
            queryLimit: $queryLimit
            projectId: $projectId
        ) {
            count
            documents {
                id
                activeState
                documentType
                created
                projectId
                name
                description
                accountNumber
                group
                externalId
                tagIds
                toForecast
                isAccrual
                accrualToForecast
                contractCount
                changeOrderCount
                costs {
                    parentId
                    expected
                    actual
                    adjusted
                    invoiced
                    remaining
                    surcharge
                    withheld
                }
                contractCosts {
                    parentId
                    expected
                    actual
                    adjusted
                    invoiced
                    remaining
                    surcharge
                    withheld
                }
                subContractorCosts {
                    parentId
                    expected
                    actual
                    adjusted
                    invoiced
                    remaining
                    surcharge
                    withheld
                }
                forecast
                forecastData {
                    accountBudget
                    accountAdjustedBudget
                    accrualTotal
                    accrualBudget
                    accrualCost
                    accrualForecast
                    purchase
                    contractBudget
                    contractProcured
                    subContractor
                    subContractorApproved
                    counterClaim
                    counterClaimApproved
                    client
                    clientApproved
                    risk
                    riskToForecast
                    expected
                    produced
                }
            }
        }
    }
'''

QUERY_AIMZ_COMPANIES = '''
    query companies($queryOffset: Int, $queryLimit: Int, $organizationNumber: [String], $externalId: [String]) {
        companies(queryOffset: $queryOffset, queryLimit: $queryLimit, organizationNumber: $organizationNumber, externalId: $externalId) {
            count
            documents {
                id
                activeState
                documentType
                created
                name
                companyType
                organizationNumber
                vatCode
                externalId
            }
        }
    }
'''

QUERY_AIMZ_INVOICES = '''
    query invoices(
        $queryOffset: Int
        $queryLimit: Int
        $ids: [UUID]
        $projectId: [String]
        $accountId: [String]
        $companyId: [String]
        $invoiceType: [InvoiceType]
        $invoiceNumber: [String]
        $externalProvider: [String]
        $externalId: [String]
        $externalIdMissingWithProvider: [Boolean]
        $status: [InvoiceStatus]
        $approvedStatus: [InvoiceApprovedStatus]
        $isParent: [Boolean]
        $invoiceDateFrom: DateTime
        $invoiceDateTo: DateTime
        ) {
        invoices(
            queryOffset: $queryOffset
            queryLimit: $queryLimit
            ids: $ids
            projectId: $projectId
            accountId: $accountId
            companyId: $companyId
            invoiceType: $invoiceType
            invoiceNumber: $invoiceNumber
            externalProvider: $externalProvider
            externalId: $externalId
            externalIdMissingWithProvider: $externalIdMissingWithProvider
            status: $status
            approvedStatus: $approvedStatus
            isParent: $isParent
            invoiceDateFrom: $invoiceDateFrom
            invoiceDateTo: $invoiceDateTo
        ) {
            count
            documents {
                id
                activeState
                documentType
                created
                projectId
                accountId
                parentDocumentType
                parentDocumentId
                companyId
                status
                approvedStatus
                parameterOverrides
                overridesUsed
                invoiceIsSplit
                invoiceIsSplitManually
                isParent
                parentId
                externalProvider
                externalId
                externalReferenceId
                externalAttachmentId
                externalRegisteredReferenceId
                externalIdMissingWithProvider
                externalProjectId
                externalAccountId
                externalCompanyId
                invoiceType
                invoicePaymentType
                invoiceNumber
                vatCode
                vatAmount
                invoiceDate
                voucherDate
                dueDate
                comments
                currencyCode
                exchangeRate
                amount
                withheld
            }
        }
    }
'''

QUERY_AIMZ_CHANGE_ORDERS = '''
  query changeOrders($queryOffset: Int, $queryLimit: Int, $projectId: [String]) {
    changeOrders(queryOffset: $queryOffset, queryLimit: $queryLimit, projectId: $projectId) {
      count
      documents {
        id
        activeState
        documentType
        created
        changed
        changedBy
        createdBy
        projectId
        contractId
        companyId
        internalChangeId
        expectedChangeId
        contractOptionId
        clientChangeIds
        contractorChangeIds
        accountIds
        expectedChangeIds
        publish
        name
        description
        basis
        basisOptions
        color
        changeOrderType
        group
        revision
        groundsForRejection
        expected
        sent
        received
        replied
        revised
        status
        actionResponsible
        consequence
        surchargePercent
        costs {
          id
          parentId
          subContractorId
          externalId
          name
          expected
          actual
          adjusted
          invoiced
          remaining
          surcharge
          withheld
        }
        clientCost
        accountCosts {
          id
          parentId
          subContractorId
          externalId
          name
          color
          expected
          actual
          adjusted
          invoiced
          remaining
          surcharge
          withheld
        }
        unitCosts {
          id
          parentId
          name
          unitType
          units
          costPerUnit
          totalCost
        }
        externalProvider
        externalId
        externalIdMissingWithProvider
        externalCosts {
          id
          parentId
          subContractorId
          externalId
          name
          color
          expected
          actual
          adjusted
          invoiced
          remaining
          surcharge
          withheld
        }
        externalProjectId
        externalCompanyId
      }
    }
  }
'''

QUERY_AIMZ_CONTRACTS = '''
  query contracts($queryOffset: Int, $queryLimit: Int, $projectId: [String]) {
    contracts(queryOffset: $queryOffset, queryLimit: $queryLimit, projectId: $projectId) {
      count
      documents {
        id
        activeState
        documentType
        created
        projectId
        companyId
        name
        contractType
        contractStatus
        contractModel
        accountIds
        description
        procuredToForecast
        indexAdjusted
        startDate
        endDate
        unitCosts {
          id
          parentId
          name
          unitType
          units
          costPerUnit
          totalCost
        }
        costs {
          id
          parentId
          subContractorId
          externalId
          externalProvider
          name
          color
          expected
          adjusted
          actual
          invoiced
          withheld
          remaining
          surcharge
        }
        accountCosts {
          id
          parentId
          subContractorId
          externalId
          externalProvider
          name
          color
          expected
          adjusted
          actual
          invoiced
          withheld
          remaining
          surcharge
        }
        contractOptions {
          id
          parentId
          name
          description
          status
          cost {
            expected
          }
        }
        subContractorCosts {
          id
          parentId
          subContractorId
          name
          expected
          actual
          adjusted
          invoiced
          remaining
          surcharge
          withheld
        }
        forecast
        forecastData {
          accountBudget
          accountAdjustedBudget
          accrualBudget
          accrualCost
          accrualForecast
          purchase
          contractBudget
          contractProcured
          subContractor
          subContractorApproved
          counterClaim
          counterClaimApproved
          client
          clientApproved
          clientInvoiced
          clientWithheld
          risk
          riskToForecast
          opportunity
          opportunityToForecast
          expected
          produced
          indexExpense
          indexExpenseInvoiced
          indexIncome
          indexIncomeInvoiced
        }
        taskIds
      }
    }
  }
'''

QUERY_FILE_STORE_FILES = '''
query storageFiles(
            $searchIndexStart: Int, 
            $searchIndexStop: Int, 
            $searchKey: String, 
            $id: UUID, 
            $filename: String, 
            $key: String, 
            $changed: DateTime, 
            $changedBy: String, 
            $tags: [String], 
            $includeContent: Boolean) {
        storageFiles(
            searchIndexStart: $searchIndexStart, 
            searchIndexStop: $searchIndexStop, 
            searchKey: $searchKey, 
            id: $id, 
            filename: $filename, 
            key: $key, 
            changed: $changed, 
            changedBy: $changedBy, 
            tags: $tags, 
            includeContent: $includeContent) {
        id
        filename
        key
        changed
        changedBy
        metaData
        content
        tags
    }
}
'''

QUERY_EXTERNAL_INVOICE_IMAGES = '''
query externalInvoiceImages($externalId: String!, $externalProvider: ExternalProvider!, $settingId: String, $settingOverrides: JSONString) {
    externalInvoiceImages(externalId: $externalId, externalProvider: $externalProvider, settingId: $settingId, settingOverrides: $settingOverrides) {
        settingId
        externalId
        externalProvider
        image
        imagePage
        imagesInTotal
    }
}
'''