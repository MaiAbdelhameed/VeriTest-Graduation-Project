//conditional expressions
module or9 (
  input a,
  input b,
  output reg out
);
    always @(*) begin
        out = (a == 1'b0 && b == 1'b0) ? 1'b0 : 1'b1; // Check both bits are low
    end

endmodule
