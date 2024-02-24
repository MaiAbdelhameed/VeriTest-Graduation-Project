module priority_encoder4x2_structural_loop(input [3:0] in, output [1:0] out);

    wire [1:0] temp;

    assign temp[0] = (in[3]) ? 1'b1 : (in[2]) ? 1'b0 : (in[1]) ? 1'b1 : (in[0]) ? 1'b0 : 1'b0;
    assign temp[1] = (in[3]) ? 1'b1 : (in[2]) ? 1'b1 : (in[1]) ? 1'b0 : (in[0]) ? 1'b0 : 1'b0;

    integer i;
    always @* begin
        for (i = 0; i < 2; i = i + 1) begin
            case(temp)
                2'b01: out = {1'b0, temp[0]};
                2'b11: out = temp;
                default: out = 2'b00; // Handle undefined case
            endcase
        end
    end

endmodule
