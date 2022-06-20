from brownie import accounts, network, config
from web3 import Web3

FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local", "hardhat"]


def get_account(index=None, id=None):
    if index:
        return accounts[index]   
    if id:
        return accounts.load(id)
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS or \
       network.show_active() in FORKED_LOCAL_ENVIRONMENTS:
        return accounts[0]
    return accounts.add(config["wallets"]["from_key"])

contract_to_mock = {
    "eth_usd_price_feed": 1,
}

# def get_contract(contract_name):
#     """
#     Grab the contract address from the brownie config if defined,
#     otherwise, it will deploy a mock version of that contract, and 
#     return that mock contract.
#         Args:
#             contract_name (string)
#         Returns:
#             brownie.network.contract.ProjectContract: The most recently
#             deployed version of this contract.
#             Contract_[-1]
#     """
#     contract_type = contract_to_mock[contract_name]
#     if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
#         if len(contract_type) <= 0:
#             deploy_mocks()
#         contract = contract_type[-1]
#     else:
#         contract_address = config["networks"][network.show_active()][contract_name]
#         contract = Contract.from_abi(contract_type._name, contract_address, contract_type.abi)
#     return contract


# def deploy_mocks(decimals=DECIMALS, starting_price=STARTING_PRICE):
#         print("Starting deploy Mock...")
#         account = get_account()
#         MockV3Aggregator.deploy(decimals, starting_price, {"from": account})
#         link_token = LinkToken.deploy({"from": account})
#         VRFCoordinatorMock.deploy(link_token.address, {"from": account})
#         print(f"Mock has been deployed. Network: {network.show_active()}, account: {account}", "\n")
