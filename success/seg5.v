//Verilog module.
module seg5(
    bcd,
    seg
    );
    
     //Declare inputs,outputs and internal variables.
    input [3:0] bcd;
    output [6:0] seg;
    reg [6:0] seg;

//always block for converting bcd digit into 7 segment format
    always @(bcd)
    begin
        if(bcd == 0)
            seg = 7'b1111110;
        else if(bcd == 1)
            seg = 7'b0110000;
        else if(bcd == 2)
            seg = 7'b1101101;
        else if(bcd == 3)
            seg = 7'b1111001;
        else if(bcd == 4)
            seg = 7'b0110011;
        else if(bcd == 5)
            seg = 7'b1011011;
        else if(bcd == 6)
            seg = 7'b1011111;
        else if(bcd == 7)
            seg = 7'b1110000;
        else if(bcd == 8)
            seg = 7'b1111111;
        else if(bcd == 9)
            seg = 7'b1111011;
        else
            seg = 7'b0000000; 
    end
    
endmodule