pragma solidity >=0.7.0 <0.8.0;

     
    contract DealContract{
        uint private hour_rate=0;
        uint private durations=0;
        uint private number_of_leaves_allowed=0;
        uint private extra_leave_penalty=0;
        bool private order_delivered=false;
        bool private payment_done=false;
        bool private in_progress=false;
        string private employer="none";
        string private employee="none";
        uint private isbonusapplicable=0;
        uint private leaves_taken=0;
        uint private hours_worked=0;
        uint private bonus_amount=0;
        uint private over_due_charge=0;
        function setdata(string memory Employer,string memory Employee,uint nola,uint elp,uint hr,uint isbonus,uint duration,uint bonusamount,uint overdue)public payable {
            employer=Employer;
            employee=Employee;
            in_progress=true;
            number_of_leaves_allowed=nola;
            extra_leave_penalty=elp;
            hour_rate=hr;
            isbonusapplicable=isbonus;
            durations=duration;
            bonus_amount=bonusamount;
            over_due_charge=overdue;
        }
        function setpostcontractdata(uint leaves,uint hoursworked)public payable {
            hours_worked=hoursworked;
            leaves_taken=leaves;
            in_progress=false;
            
        }
        function calculate_amount()public view returns(uint){
            uint initial_amount=0;
            if(hours_worked>durations){
                initial_amount=hour_rate*durations;
                initial_amount=initial_amount-over_due_charge;
            }
            if(hours_worked<durations){
                 initial_amount=hour_rate*hours_worked;
            }
           
            if(leaves_taken>number_of_leaves_allowed){
                uint extraleaves=leaves_taken-number_of_leaves_allowed;
                initial_amount=initial_amount-(extraleaves*extra_leave_penalty);
            }
            if(isbonusapplicable==1){
                initial_amount+=bonus_amount;
            }
            return initial_amount;
            
            
        }
        function setorderstatus()public payable returns(bool){
            order_delivered=true;
            return true;
        }
        function setpaymentstatus()public payable returns(bool){
            payment_done=true;
            return true;
        }
        
        
    }