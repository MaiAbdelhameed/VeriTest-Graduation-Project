module decoder2 (en,a,b,y);
    input en,a,b;   
    output reg [3:0]y;

    always @(en,a,b)
    begin
        if(en==0)
        begin
            if(a==1'b0 & b==1'b0) y=4'b1110;
            else if(a==1'b0 & b==1'b1) y=4'b1101;
            else if(a==1'b1 & b==1'b0) y=4'b1011;
            else if(a==1 & b==1) y=4'b0111;
        end
        else
        y=4'b1111;
    end
endmodule