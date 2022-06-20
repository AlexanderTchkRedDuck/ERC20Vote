from brownie import ERC20Vote, network, config
from scripts.helpful_scripts import get_account
from web3 import Web3
import time

initialSupply = 8

def deploy_ERC20Vote():
    print("Staring deploy ERC20Vote...")
    account = get_account()
    lottery = ERC20Vote.deploy(
        10,             #initialSupply
        "REDTOKEN",     #name_
        "RDT",          #symbol_
        "2",            #price_
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify", False)
    )
    print("Deployed ERC20Vote!!!")
    return lottery

def start_voting():
    account = get_account()
    lottery = ERC20Vote[-1]
    suggested_price = 4
    duration = 60
    starting_tx = lottery.startVoting(suggested_price, duration, {"from": account})
    starting_tx.wait(1)
    print("Voting is started!!!")

def buy_token(index, value):
    print("Buying the token!")
    account = get_account(index)
    voting = ERC20Vote[-1]
    threshold_to_vote = voting.getThresholdToVote({"from": account})
    print(f"Threshold to vote is: {threshold_to_vote}")
    print(f"voting.getPrice() is: {voting.getPrice()}")
    # voting.buy_token({"from": account, "value": value})
    # voting.vote({"from": account})
    # tx = lottery.enter({"from": account})
    # tx.wait(1)
    print("You enter the lottery!")

def vote():
    account = get_account(index=1)
    buy_token(index=1, value=2)
    lottery = ERC20Vote[-1]
    threshold_to_vote = lottery.getThresholdToVote()
    print(threshold_to_vote)
    vote = lottery.vote({"from": account})
    # tx = lottery.enter({"from": account})
    # tx.wait(1)
    print("You enter the lottery!")

# def end_voting():
#     account = get_account()
#     lottery = ERC20Vote[-1]
#     # Fund the contract
#     ending_transaction = lottery.endLottery({"from": account})
#     ending_transaction.wait(1)
#     time.sleep(60)
#     print(f"{lottery.recentWinner()} is new winner")

def main():
    deploy_ERC20Vote()
    start_voting()
    vote()
    # end_voting()