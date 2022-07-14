# Connext Low Gas Usage

## Description

This agent detects low gas usage for the specified contracts in specified chains.

## Supported Chains

- all chains are supported

## Setup

Please specify the contracts and the thresholds in the `src/config.py`

```python
target_contracts_by_chain = {CHAIN_ID_1: {"lowercase_contract_address_1": "Contract Name 1",
                                          "lowercase_contract_address_2": "Contract Name 2"},
                             CHAIN_ID_2: {"lowercase_contract_address_3": "Contract Name 3",
                                          "lowercase_contract_address_4": "Contract Name 4"}}

GAS_TH_BY_CHAIN = {CHAIN_ID_1: int_1,
                   CHAIN_ID_2: int_2}
GAS_HIGH_TH_BY_CHAIN = {CHAIN_ID_1: int_1,
                        CHAIN_ID_2: int_2}
GAS_CRITICAL_TH_BY_CHAIN = {CHAIN_ID_1: int_1,
                            CHAIN_ID_2: int_2}
```

## Alerts

- CONNEXT_LOW_GAS
    - Fired when a transaction's gas in less than threshold
    - Severity depends on the gas:
        - `Critical` if the gas is below critical gas threshold
        - `High` if the gas is below high gas threshold
        - `Medium` if the gas is below gas threshold
    - Type is always set to "Suspicious"
    - Metadata contains:
        - `timestamp`: timestamp of the block that contains suspicious transaction
        - `gas`: the amount of used gas
        - `contract_address`: contact address related to the transaction
        - `sender`: sender of the transaction
