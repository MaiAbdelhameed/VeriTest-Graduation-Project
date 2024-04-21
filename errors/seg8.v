//Verilog module.
module seg8(
    w,x,y,z,
    a,b,c,d,e,f,g
    );
    
     //Declare inputs,outputs and internal variables.
    input w,x,y,z;
    output reg a,b,c,d,e,f,g;

//always block for converting bcd digit into 7 segment format
    always @(*)
    begin
        if ({w,x,y,z} == 4'b0000)
            {a,b,c,d,e,f,g} = 7'b1111110;
        else if({w,x,y,z} == 4'b0001)
            {a,b,c,d,e,f,g} = 7'b0110000;
        else if({w,x,y,z} == 4'b0010)
            {a,b,c,d,e,f,g} = 7'b1101101;
        else if({w,x,y,z} == 4'b0011)
            {a,b,c,d,e,f,g} = 7'b1111001;
        else if({w,x,y,z} == 4'b0100)
            {a,b,c,d,e,f,g} = 7'b0110011;
        else if({w,x,y,z} == 4'b0101)
            {a,b,c,d,e,f,g} = 7'b1011011;
        else if({w,x,y,z} == 4'b0110)
            {a,b,c,d,e,f,g} = 7'b1011111;
        else if({w,x,y,z} == 4'b0111)
            {a,b,c,d,e,f,g} = 7'b1110000;
        else if({w,x,y,z} == 4'b1000)
            {a,b,c,d,e,f,g} = 7'b1111111;
        else if({w,x,y,z} == 4'b1001)
            {a,b,c,d,e,f,g} = 7'b1111011;
            //switch off 7 segment character when the bcd digit is not a decimal number.
        else 
            {a,b,c,d,e,f,g} = 7'b0000000; 
    end
    
endmodule
Error occurred: 'NoneType' object has no attribute 'connections'