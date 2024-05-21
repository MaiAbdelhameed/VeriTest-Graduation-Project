module pe25 (input [3:0] in, output [1:0] out);

    reg [1:0] temp;

    always @* begin
        if(in[3]) begin
            temp[0] = 1'b1;
            temp[1] = 1'b1;
        end else if(in[2]) begin
            temp[0] = 1'b0;
            temp[1] = 1'b1;
        end else if(in[1]) begin
            temp[0] = 1'b1;
            temp[1] = 1'b0;
        end else if(in[0]) begin
            temp[0] = 1'b0;
            temp[1] = 1'b0;
        end else begin
            temp[0] = 1'b0;
            temp[1] = 1'b0;
        end


    end

    assign out = (temp[1] == 1'b1) ? temp : (temp[0] == 1'b1) ? {1'b0, temp[0]} : 2'b00;

endmodule