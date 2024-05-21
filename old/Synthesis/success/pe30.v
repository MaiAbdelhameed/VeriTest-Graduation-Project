module pe30 (input [3:0] in, output [1:0] out);

    reg [1:0] temp;
    always @* begin
        if (in[3] == 1'b1) begin
            temp = {1'b1, 1'b1};
        end else if (in[2] == 1'b1) begin
            temp = {1'b1, 1'b0};
        end else if (in[1] == 1'b1) begin
            temp = {1'b0, 1'b1};
        end else if (in[0] == 1'b1) begin
            temp = {1'b0, 1'b0};
        end else begin
            temp = 2'b00;
        end
    end

    assign out = temp;

endmodule
