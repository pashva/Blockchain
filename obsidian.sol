pragma solidity >=0.7.0 <0.8.0;

     
    contract Obsidian{
       uint public max_obsidians=1000000000;
       uint public inr_obsidians=2;
       uint public total_obsidian_bought=0;
       mapping(address=>uint) equity_obsidian;
      
       
       modifier is_obsidian_available(uint inr_invested){
           require(inr_invested*inr_obsidians+total_obsidian_bought<=max_obsidians);
           _;
       }
        modifier is_sender_valid(address sender){
           require(msg.sender==sender);
           _;
       }
       function equity_in_obsidian(address investor)public view returns(uint){
           return equity_obsidian[investor];
       }
     
       function buy_obsidians(address investor,uint inr_invested)external is_obsidian_available(inr_invested){
           uint obs_bought=inr_invested*inr_obsidians;
           equity_obsidian[investor]=equity_obsidian[investor]+obs_bought;
         
           total_obsidian_bought+=obs_bought;
       }
       
       function transfer_obsidian(address seller,address buyer,uint amount)external is_sender_valid(seller){
           equity_obsidian[seller]=equity_obsidian[seller]-amount;
           equity_obsidian[buyer]=equity_obsidian[buyer]+amount;
           
       }
       
    }