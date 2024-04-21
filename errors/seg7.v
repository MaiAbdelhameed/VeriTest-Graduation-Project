//Verilog module.
module seg7(
    w,x,y,z,
    a,b,c,d,e,f,g
    );
    
     //Declare inputs,outputs and internal variables.
    input w,x,y,z;
    output reg a,b,c,d,e,f,g;

//always block for converting bcd digit into 7 segment format
    always @(*)
    begin
        case ({w,x,y,z}) //case statement
            4'b0000 : {a,b,c,d,e,f,g} = 7'b1111110;
            4'b0001 : {a,b,c,d,e,f,g} = 7'b0110000;
            4'b0010 : {a,b,c,d,e,f,g} = 7'b1101101;
            4'b0011 : {a,b,c,d,e,f,g} = 7'b1111001;
            4'b0100 : {a,b,c,d,e,f,g} = 7'b0110011;
            4'b0101 : {a,b,c,d,e,f,g} = 7'b1011011;
            4'b0110 : {a,b,c,d,e,f,g} = 7'b1011111;
            4'b0111 : {a,b,c,d,e,f,g} = 7'b1110000;
            4'b1000 : {a,b,c,d,e,f,g} = 7'b1111111;
            4'b1001 : {a,b,c,d,e,f,g} = 7'b1111011;
            //switch off 7 segment character when the bcd digit is not a decimal number.
            default : {a,b,c,d,e,f,g} = 7'b0000000; 
        endcase
    end
    
endmodule
Error occurred: 'NoneType' object has no attribute 'connections'