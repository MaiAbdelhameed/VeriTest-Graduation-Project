module xnor8 (
  input a,
  input b,
  output reg out
);

    always @(*) begin
        out = (a == b) ? 1'b1 : 1'b0; // XNOR using conditional expression (XOR and invert both)
    end
    
endmodule
