module decoder30 (a,b,en,y);
    input a,b,en;   
    output reg [3:0] y;

    always @(en,a,b)
    begin
        if(a==1'b0 & b==1'b0) y=4'b1110;
            else if(a==1'b0 & b==1'b1) y=4'b1101;
            else if(a==1'b1 & b==1'b0) y=4'b1011;
            else if(a==1 & b==1) y=4'b0111;
    end
endmodule