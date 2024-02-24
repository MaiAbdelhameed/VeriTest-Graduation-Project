/////check/////

module decoder3x8_structural_loop(input [2:0] in, output reg [7:0] out);

    reg [7:0] temp;

    integer i;
    always @* begin
        for (i = 0; i < 8; i = i + 1) begin
            case(in)
                3'b000: temp = 8'b00000001;
                3'b001: temp = 8'b00000010;
                3'b010: temp = 8'b00000100;
                3'b011: temp = 8'b00001000;
                3'b100: temp = 8'b00010000;
                3'b101: temp = 8'b00100000;
                3'b110: temp = 8'b01000000;
                3'b111: temp = 8'b10000000;
                default: temp = 8'b00000000; // Handle undefined case
            endcase
        end
    end

    assign out = temp;

endmodule
