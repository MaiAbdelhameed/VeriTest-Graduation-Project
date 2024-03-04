module decoder31 (
    input [4:0] select,
    output reg [31:0] output
);

always @(*) begin
    case(select)
        5'd0: output = 32'b00000000000000000000000000000001;
        5'd1: output = 32'b00000000000000000000000000000010;
        5'd2: output = 32'b00000000000000000000000000000100;
        5'd3: output = 32'b00000000000000000000000000001000;
        5'd4: output = 32'b00000000000000000000000000010000;
        5'd5: output = 32'b00000000000000000000000000100000;
        5'd6: output = 32'b00000000000000000000000001000000;
        5'd7: output = 32'b00000000000000000000000010000000;
        5'd8: output = 32'b00000000000000000000000100000000;
        5'd9: output = 32'b00000000000000000000001000000000;
        5'd10: output = 32'b00000000000000000000010000000000;
        5'd11: output = 32'b00000000000000000000100000000000;
        5'd12: output = 32'b00000000000000000001000000000000;
        5'd13: output = 32'b00000000000000000010000000000000;
        5'd14: output = 32'b00000000000000000100000000000000;
        5'd15: output = 32'b00000000000000001000000000000000;
        5'd16: output = 32'b00000000000000010000000000000000;
        5'd17: output = 32'b00000000000000100000000000000000;
        5'd18: output = 32'b00000000000001000000000000000000;
        5'd19: output = 32'b00000000000010000000000000000000;
        5'd20: output = 32'b00000000000100000000000000000000;
        5'd21: output = 32'b00000000001000000000000000000000;
        5'd22: output = 32'b00000000010000000000000000000000;
        5'd23: output = 32'b00000000100000000000000000000000;
        5'd24: output = 32'b00000001000000000000000000000000;
        5'd25: output = 32'b00000010000000000000000000000000;
        5'd26: output = 32'b00000100000000000000000000000000;
        5'd27: output = 32'b00001000000000000000000000000000;
        5'd28: output = 32'b00010000000000000000000000000000;
        5'd29: output = 32'b00100000000000000000000000000000;
        5'd30: output = 32'b01000000000000000000000000000000;
        5'd31: output = 32'b10000000000000000000000000000000;
    endcase
end

endmodule
