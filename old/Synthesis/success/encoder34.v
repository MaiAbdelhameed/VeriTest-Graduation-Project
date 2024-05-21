module encoder34 (input [1:0] in, output [1:0] out);

    reg [1:0] temp;

    integer i;
    always @* begin
        for (i = 0; i < 2; i = i + 1) begin
            case(in[i])
                1: temp[i] = 1'b1;
                default: temp[i] = 1'b0;
            endcase
        end
    end

    assign out = temp;

endmodule
