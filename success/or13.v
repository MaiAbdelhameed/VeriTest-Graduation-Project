//case statements
module or13 (
  input a,
  input b,
  output reg out
);


    always @(*) begin
        case ({a, b})
            2'b01, 2'b10, 2'b11: out = 1'b1;
            default: out = 1'b0;
        endcase
    end

endmodule

