module pe29 (input [3:0] in, output reg [1:0] out);

    always @* begin
        if (in[3] == 1'b1) begin
            out = {1'b1, 1'b1};
        end else if (in[2] == 1'b1) begin
            out = {1'b1, 1'b0};
        end else if (in[1] == 1'b1) begin
            out = {1'b0, 1'b1};
        end else if (in[0] == 1'b1) begin
            out = {1'b0, 1'b0};
        end else begin
            out = 2'b00;
        end
    end

endmodule
