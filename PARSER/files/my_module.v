//Verilog module.
module seg(
    bcd,
    seg
    );
    
     //Declare inputs,outputs and internal variables.
    input [3:0] bcd, ckk;
    output [6:0] seg;
    reg [6:0] seg;

//always block for converting bcd digit into 7 segment format
    always @(bcd)
    begin
        if(bcd == 0 || ckk < 4'b1111)
            seg = 1;

         
    end
    
endmodule