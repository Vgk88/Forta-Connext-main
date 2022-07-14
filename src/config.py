# Specify the contracts and networks that should be monitored using format
# {CHAIN_ID_1: {"lowercase_contract_address_1": "Contract Name 1",
#               "lowercase_contract_address_2": "Contract Name 2"},
#  CHAIN_ID_2: {"lowercase_contract_address_3": "Contract Name 3",
#               "lowercase_contract_address_4": "Contract Name 4"}}
target_contracts_by_chain = {1: {'0x': "ContractName"}, }

# Specify the gas threshold by chain using format
# {CHAIN_ID_1: int_1,
#  CHAIN_ID_2: int_2}
GAS_TH_BY_CHAIN = {1: 35000}
GAS_HIGH_TH_BY_CHAIN = {1: 28000}
GAS_CRITICAL_TH_BY_CHAIN = {1: 21000}
