from brownie import ERC20Vote, accounts, config, network, exceptions
from web3 import Web3
import pytest
from scripts.deploy import deploy_ERC20Vote, buy_token, INITIAL_PRICE, INITIAL_SUPPLY
from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENVIRONMENTS, get_account
import time

NORMOLIZE = 10 ** -18
SUGGESTED_PRICE = 1
DURATION = 5
NUMBER_OF_PARTICIPANTS = 5

def test_voting_process():
    # Arrange
    # Deploying
    account = get_account()
    vote = deploy_ERC20Vote()
    total_tokens_vots = 0
    vote.startVoting(SUGGESTED_PRICE, DURATION, {"from": account})
    total_tokens_vots += vote.balanceOf(account)
    # Voting
    price = vote.getPrice() * NORMOLIZE
    amount_of_purchased_tokens = vote.getThresholdToVote() * 1.1 #Have to increase, becouse threshold will be increased
    eth_amount = price * amount_of_purchased_tokens
    voting_accounts = {}

    for i in range(1, NUMBER_OF_PARTICIPANTS + 1):
            account = get_account(index=i)
            buy_token(account, value=(eth_amount * float(f"1.{i}")))
            voting_accounts[i] = account
            total_tokens_vots += vote.balanceOf(account)
            vote.vote({"from": account})
            assert vote.alreadyVoted(account) == True
            assert vote._currentNumberVotesToChangePrice() == total_tokens_vots
    time.sleep(7)
    # vote.endVoting()
    # assert vote.voteState() == 1


    


    
 















