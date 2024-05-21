//Verilog module.
module seg6(
    bcd,
    a,b,c,d,e,f,g
    );
    
     //Declare inputs,outputs and internal variables.
    input [3:0] bcd;
    output reg a,b,c,d,e,f,g;

//always block for converting bcd digit into 7 segment format
    always @(bcd)
    begin
        if(bcd == 0)
            {a,b,c,d,e,f,g} = 7'b1111110;
        else if(bcd == 1)
            {a,b,c,d,e,f,g}  = 7'b0110000;
        else if(bcd == 2)
            {a,b,c,d,e,f,g}  = 7'b1101101;
        else if(bcd == 3)
            {a,b,c,d,e,f,g}  = 7'b1111001;
        else if(bcd == 4)
            {a,b,c,d,e,f,g}  = 7'b0110011;
        else if(bcd == 5)
            {a,b,c,d,e,f,g}  = 7'b1011011;
        else if(bcd == 6)
            {a,b,c,d,e,f,g}  = 7'b1011111;
        else if(bcd == 7)
            {a,b,c,d,e,f,g}  = 7'b1110000;
        else if(bcd == 8)
            {a,b,c,d,e,f,g}  = 7'b1111111;
        else if(bcd == 9)
            {a,b,c,d,e,f,g}  = 7'b1111011;
        else
            {a,b,c,d,e,f,g}  = 7'b0000000; 
    end
    
endmodule