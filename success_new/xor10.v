module xor10 (
  input a,
  input b,
  input c,
  output reg out
);

    always @(*) begin
        out = (^{a,b,c}); // XNOR using built-in operator
    end
    
    
endmodule
