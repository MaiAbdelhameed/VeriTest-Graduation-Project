module encoder20(a0,a1,a2,a3,en,y0,y1);
    input a0,a1,a2,a3;
    input en;
    output reg y0,y1;
    always@(*)
    begin
        if(!en)
            {y1,y0} =2'b00;
        else
        case({a3,a2,a1,a0})
            4'b0001:
                {y1,y0} = 2'b00;
            4'b0010:
                {y1,y0} = 2'b01;
            4'b0100: 
                {y1,y0} = 2'b10;
            4'b1000:
                {y1,y0} = 2'b11;
            default: {y1,y0} = 2'b00;
        endcase
    end
endmodule