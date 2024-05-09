module pe24 (input [3:0] in, output [1:0] out);

    reg [1:0] temp;

    always @* begin
        temp[0] = (in[3]) ? 1'b1 : (in[2]) ? 1'b0 : (in[1]) ? 1'b1 : (in[0]) ? 1'b0 : 1'b0;
        temp[1] = (in[3]) ? 1'b1 : (in[2]) ? 1'b1 : (in[1]) ? 1'b0 : (in[0]) ? 1'b0 : 1'b0;
    end

    assign out = (temp[1] == 1'b1) ? temp : (temp[0] == 1'b1) ? {1'b0, temp[0]} : 2'b00;

endmodule
