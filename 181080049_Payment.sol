// SPDX-License-Identifier: MIT
pragma solidity >=0.7.0 <0.9.0;

contract Payment {

    
    enum BillStatus { Paid, Unpaid }
    BillStatus paymentStatus;
    address payable public vendor;
    uint256 amountToBePaid;

    event paymentSuccess(address _buyer, uint _value);

    constructor() {
        vendor = payable(msg.sender);
        paymentStatus = BillStatus.Unpaid;
    }
    
     modifier amountIsValid {
        require(paymentStatus == BillStatus.Unpaid, "The Bill is already paid and there is no amount pending!");
        require(msg.value >= amountToBePaid, "The transaction did not go through because the amount was less than the required bill value.");
        _;
    }

    function setAmountToBePaid(uint256 _amountToBePaid) public {
        require(msg.sender == vendor, "Only the vendor can set the Bill Amount");
        amountToBePaid = _amountToBePaid;
        paymentStatus = BillStatus.Unpaid;
    }
    
    function billPaymentStatus() public view returns (string memory) {
        if(paymentStatus == BillStatus.Paid){
            return "Paid";
        }
        else {
            return "Unpaid";
        }
    }

    function sendPayment() public payable amountIsValid {
        paymentStatus = BillStatus.Paid;
        vendor.transfer(msg.value);
        emit paymentSuccess(msg.sender, msg.value);
    }
    
}