# from brownie import ERC20Vote, accounts, config, network, exceptions
# from web3 import Web3
# import pytest
# from scripts.deploy import deploy_ERC20Vote, buy_token, INITIAL_PRICE, INITIAL_SUPPLY
# from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENVIRONMENTS, get_account

# NORMOLIZE = 10 ** -18
# SUGGESTED_PRICE = 1
# DURATION = 60

# def test_threshold_to_vote_amount():
#     # Arrange 
#     vote = deploy_ERC20Vote()
#     threshold_to_vote = Web3.toWei(INITIAL_SUPPLY, "ether") * 0.05
#     # Act
#     getThresholdToVote = vote.getThresholdToVote()
#     # Assert
#     assert  getThresholdToVote == threshold_to_vote

# def test_buing_tokens():
#     # Arrange
#     vote = deploy_ERC20Vote()
#     account = get_account(index=1)
#     price = vote.getPrice() * NORMOLIZE
#     amount_of_purchased_tokens = Web3.toWei(1, "ether")
#     eth_amount = price * amount_of_purchased_tokens
#     # Act
#     buy_token(account, value=eth_amount) 
#     # Assert
#     assert vote.balanceOf(account) == amount_of_purchased_tokens

# def test_requirements_before_startVoting():
#     # Arrange
#     vote = deploy_ERC20Vote()
#     account = get_account()
#     # Act/Assert
#     assert vote.voteState() == 2
#     assert vote.balanceOf(account) > vote.getThresholdToVote()

# def test_startVoting():
#     # Arrange
#     vote = deploy_ERC20Vote()
#     account = get_account(index=1)
#     price = vote.getPrice() * NORMOLIZE
#     amount_of_purchased_tokens = vote.getThresholdToVote() * 1.1 #Have to increase, becouse threshold will be increased
#     eth_amount = price * amount_of_purchased_tokens
#     # TODO
#     # Ask a question about 'price' and changing getThresholdToVote after buying tokens
#     # Act
#     buy_token(account, value=(eth_amount))
#     vote.startVoting(SUGGESTED_PRICE, DURATION, {"from": account})
#     # Assert
#     assert vote.balanceOf(account) >= vote.getThresholdToVote()
#     assert vote.voteState() == 0
#     # TODO: Why we got additional 50???
#     #assert vote._currentNumberVotesToChangePrice() == amount_of_purchased_tokens
#     assert vote._suggestedPrice() == SUGGESTED_PRICE
#     assert vote._duration() == DURATION
#     assert vote.alreadyVoted(account) == True

# def test_vote_without_starting():
#     # Arrange
#     vote = deploy_ERC20Vote()
#     account = get_account(index=1)
#     # ACT / Assert
#     with pytest.raises(exceptions.VirtualMachineError):
#         vote.vote({"from": account})

# def test_close_vote_without_starting():
#     # Arrange
#     vote = deploy_ERC20Vote()
#     account = get_account(index=1)
#     # ACT / Assert
#     with pytest.raises(exceptions.VirtualMachineError):
#         vote.endVoting({"from": account})

    


    
 















