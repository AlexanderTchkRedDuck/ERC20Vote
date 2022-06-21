// SPDX-License-Identifier: AGPL-3.0
pragma solidity ^0.8.9;

import "./ERC20.sol";

contract ERC20Vote is ERC20 {
    uint64 public _duration;
    uint64 public _votingStartedTime;
    uint256 public _minNumberVotesToChangePrice;
    uint256 public _currentNumberVotesToChangePrice;
    uint256 public _suggestedPrice;

    mapping(address => bool) public alreadyVoted;

    enum VOTE_STATE {
        OPEN,
        CALCULATING_WINNERS,
        CLOSED
    }
    VOTE_STATE public voteState;

    event VotingStart(
        address indexed account,
        uint256 suggestedPrice,
        uint64 duration
    );

    event Vote(address indexed account);

    event VotingEnd(
        address indexed account,
        uint256 previousPrice,
        uint256 price
    );

    constructor(
        uint256 initialSupply,
        string memory name_,
        string memory symbol_,
        uint256 price_
    ) ERC20(initialSupply, name_, symbol_, price_) {
        // setting initial minimum threshold to change price
        _minNumberVotesToChangePrice = initialSupply * 10;
        voteState = VOTE_STATE.CLOSED;
    }

    // Get 0.05 Threshold to start voting for a price change
    // or can vote for a particular price.
    function getThresholdToVote() public view returns (uint256) {
        uint256 thresholdToVote = totalSupply / 20;
        return thresholdToVote;
    }

    // Get Threshold to change a price.
    // function getThresholdToChangePrice() public view returns (uint256) {
    //     return _minNumberVotesToChangePrice;
    // }

    function startVoting(uint256 suggestedPrice_, uint64 duration)
        external
        returns (bool)
    {
        require(
            voteState == VOTE_STATE.CLOSED,
            "Voting has begun. Starting a new vote is prohibited!"
        );
        uint256 amountTokensToVote = balanceOf[msg.sender];
        require(amountTokensToVote >= getThresholdToVote());
        require(suggestedPrice_ > 0, "SuggestedPrice must be positive!");
        require(duration > 0, "Duration must be positive!");

        voteState = VOTE_STATE.OPEN;
        _currentNumberVotesToChangePrice += amountTokensToVote;
        _suggestedPrice = suggestedPrice_;
        _duration = duration;
        _votingStartedTime = _time();

        alreadyVoted[msg.sender] = true;

        emit VotingStart(msg.sender, suggestedPrice_, duration);
        return true;
    }

    function vote() external returns (bool) {
        uint64 time = _time();
        uint256 votingEndTime = _votingStartedTime + _duration;

        if (time >= votingEndTime) {
            voteState == VOTE_STATE.CALCULATING_WINNERS;
        }
        require(
            voteState == VOTE_STATE.OPEN,
            "Voting is closed! To vote, start a new vote!"
        );
        require(balanceOf[msg.sender] >= getThresholdToVote());
        require(!alreadyVoted[msg.sender], "You have already voted!");

        alreadyVoted[msg.sender] = true;
        _currentNumberVotesToChangePrice += balanceOf[msg.sender];

        emit Vote(msg.sender);
        return true;
    }

    function endVoting() external returns (bool) {
        uint64 time = _time();
        uint256 votingEndTime = _votingStartedTime + _duration;

        if (time >= votingEndTime) {
            voteState == VOTE_STATE.CALCULATING_WINNERS;
        }
        require(
            voteState == VOTE_STATE.CALCULATING_WINNERS,
            "Voting is not over yet. Closing the vote is prohibited!"
        );

        if (_currentNumberVotesToChangePrice > _minNumberVotesToChangePrice) {
            emit VotingEnd(msg.sender, _price, _suggestedPrice);
            _price = _suggestedPrice;
            _minNumberVotesToChangePrice = _currentNumberVotesToChangePrice;
        }

        delete _duration;
        delete _votingStartedTime;
        delete _currentNumberVotesToChangePrice;
        delete _suggestedPrice;

        return true;
    }

    function _time() internal view returns (uint64) {
        // solhint-disable-next-line not-rely-on-time
        return uint64(block.timestamp);
    }
}
