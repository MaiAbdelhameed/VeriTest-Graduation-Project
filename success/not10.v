module not10 (
  input in,
  output reg out
);


    always @(*) begin
        case (in)
            1'b0: out = 1'b1;
            default: out = 1'b0;
        endcase
    end

endmodule