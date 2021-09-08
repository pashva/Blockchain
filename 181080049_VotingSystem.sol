// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;

contract Voting {

    // Variables
    address private owner;
    uint256 private nominationPeriod;
    uint256 private votingPeriod;
    bool public isNominationAllowed=true;
    uint256 public nomineeCount=0;
    uint256 public voteCount=0;
    
    // Events that will be fired on emission
    event nominatedCandidate(address _nominee,string _slogan);
    event voteCast(address _voter,uint256 _id);
    event NominationClosed(string _statement);
    event VotingClosed(string _statement);
    
    // Constructor to initialise user specific fiels
    constructor(uint256 _nominationTime,uint256 _votingTime){
      nominationPeriod = block.timestamp + (_nominationTime)*1 minutes;
      votingPeriod = block.timestamp +  (_votingTime)*1 minutes;
      owner = msg.sender;
      
   }

    // A structure to define A Nominees Field
    struct Nominee{
        string slogan;
        address nominationAddress;
        uint256 voteCount;
    }
    //  A structure to define A Voters Field
    struct Voter{
        address voterAddress;
        uint256 votedToId;
        bool voted;
    }
   
   // A modifier to verify the participant
    modifier notOwner {
      require(msg.sender != owner, "Owner of this election cannot cast a vote.");
      _;
   }
   // A modifier to verify the owner
    modifier isOwner {
      require(msg.sender == owner, "Only the owner of this election can declare the results.");
      _;
   }
   // A modifier to check for a valid nomination period 
   modifier validNominationPeriod {
       if (block.timestamp <= nominationPeriod && isNominationAllowed){
          _;
       }else{
           isNominationAllowed=false;
           emit NominationClosed("CLOSED");
           revert("Nomination period has ended , you cannot nominate yourself in this election anymore.");
           
       }
     
   }
   // A modifier to check for a valid Voting period 
    modifier validVotingPeriod {
       if (block.timestamp <= votingPeriod && block.timestamp >= votingPeriod){
           _;
       }else{
           emit VotingClosed("CLOSED");
           if(isNominationAllowed){
               revert("The voting period of this contract has not yet started. Please wait for the nomination phase to end.");
           }else{
               revert("The Voting period has ended for this election.");
           }
       }
     
   }
   // A modifier to check for the completion of voting period
    modifier votingPeriodEnded {
       require(block.timestamp > votingPeriod);
       _;
   }
   // A modifier to put on a constraint on a number of votes by a single participant
    modifier hasNotVoted {
       require (hasVoted[msg.sender] == false , "You have already casted your vote! ");
       _;
   }
   // A modifier to put on a constraint on a number of nominations by a single participant
    modifier isNotNominated {
       require (isNominated[msg.sender] == false , "You have already nominated yourself! ");
       _;
   }
   
    // Mapping of required variables
    mapping(uint256 => Nominee) nominations;
    mapping(address => bool) isNominated;
    mapping(uint256 => Voter) voters;
    mapping(address => bool) hasVoted;
    
    // Function for a candidate to nominate himself if nomination takes place in a given time period
    function nominate(string calldata _slogan) public notOwner validNominationPeriod isNotNominated{
        isNominated[msg.sender] = true;
        nominations[nomineeCount++] = Nominee(_slogan,msg.sender,0);
        emit nominatedCandidate(msg.sender,_slogan);
    }
    
    // Function for a candidate to vote someone if voting takes place in a given time period
    function castVote(uint256 _id) public notOwner validVotingPeriod hasNotVoted isNotNominated{
        hasVoted[msg.sender] = true;
        Voter memory voter = Voter(msg.sender,_id,true);
        voters[voteCount++] = voter;
        nominations[_id].voteCount = nominations[_id].voteCount+1;
        emit voteCast(msg.sender,_id);
    }
   // Function for the owner to declare results
    function elected() public isOwner votingPeriodEnded view returns (address, uint256,string memory){
        uint256 maxCount=0;
        address electedCandidate;
        string memory slogan;
        for(uint256 i=0;i<nomineeCount;i++){
            if(nominations[i].voteCount > maxCount){
                maxCount = nominations[i].voteCount;
                electedCandidate =  nominations[i].nominationAddress;
                slogan =  nominations[i].slogan;
            }
        }
        return (electedCandidate,maxCount,slogan);
    }
    
    // Returns total nominations.
    function getNomineeCount()public view returns (uint256){
        return nomineeCount;
    }
    
    // Returns total votes.
    function getVoteCount()public view returns (uint256){
        return voteCount;
    }

    // Returns details of the person who hosted this election/contract
    function getOwner()public view returns (address){
        return owner;
    }
    
}