from forta_agent import Finding, FindingType, FindingSeverity, get_json_rpc_url
import forta_agent
from web3 import Web3

from config import target_contracts_by_chain, GAS_TH_BY_CHAIN, GAS_HIGH_TH_BY_CHAIN, GAS_CRITICAL_TH_BY_CHAIN

web3 = Web3(Web3.HTTPProvider(get_json_rpc_url()))
chain_id = web3.eth.chain_id
target_contracts = target_contracts_by_chain[chain_id]
GAS_TH = GAS_TH_BY_CHAIN[chain_id]
GAS_HIGH_TH = GAS_HIGH_TH_BY_CHAIN[chain_id]
GAS_CRITICAL_TH = GAS_CRITICAL_TH_BY_CHAIN[chain_id]


def get_severity(gas: float):
    """
    This function decides the severity of the alert
    :param gas: the amount of gas used
    :return: Severity
    """
    if gas < GAS_CRITICAL_TH:
        return FindingSeverity.Critical
    elif gas < GAS_HIGH_TH:
        return FindingSeverity.High
    else:
        return FindingSeverity.Medium


def handle_transaction(transaction_event: forta_agent.TransactionEvent):
    """
    This function handles and analyses the transaction
    :param transaction_event: Transaction event object from Forta SDK
    :return: Findings
    """
    findings = []

    # skip the transaction if it is not related to the Connext contract
    if transaction_event.to not in target_contracts.keys():
        return []

    # return the finding if the transaction's gas is less than the threshold
    if transaction_event.transaction.gas < GAS_TH:
        findings.append(Finding({
            'name': 'Connext Low Gas Usage',
            'description': f'The amount of gas in the transaction to the contract '
                           f'{target_contracts[transaction_event.to]} is less than the threshold.',
            'alert_id': f'CONNEXT_LOW_GAS',
            'type': FindingType.Suspicious,
            'severity': get_severity(transaction_event.transaction.gas),
            'metadata': {
                'timestamp': transaction_event.block.timestamp,
                'gas': transaction_event.transaction.gas,
                'contract_address': transaction_event.to,
                'sender': transaction_event.from_
            }
        }))

    return findings
