module comparator16 ( In1,In2,Gt,Lt,Eq); 

    input [7:0]  In1,In2; //The two 8-bit Inputs In1 and In2 

    output reg  Gt, Lt, Eq; //The Outputs of comparison 


    always @ (In1 or In2) //Check the state of the input lines 

    begin 

        Gt = ( In1 > In2 )? 1'b1 : 1'b0;
        Lt = ( In1 < In2 )? 1'b1 : 1'b0;
        Eq = ( In1 == In2)? 1'b1 : 1'b0; 

    end 

endmodule
