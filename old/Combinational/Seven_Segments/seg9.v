//Verilog module.
module seg9(
    w,x,y,z,
    a,b,c,d,e,f,g
    );
    
     //Declare inputs,outputs and internal variables.
    input w,x,y,z;
    output reg a,b,c,d,e,f,g;

//always block for converting bcd digit into 7 segment format
    always @(*)
    begin
        a = w + y + (x & z) + (~x & ~z);
        b = w + (~w & ~x) + (y & z) + (~y & ~z);
        c = w + (x & y) + (~x & z) + (~x & ~y);
        d = w + (y & ~z) + (~w & ~x & y) + (x & ~y & z) + (~x & ~z);
        e = (y & ~z) + (~x & ~z);
        f = w + (x & ~y) + (x & ~z) + (~y & ~z);
        g = w + (x & ~y) + (x & ~z) + (~x & y);
    end
    
endmodule