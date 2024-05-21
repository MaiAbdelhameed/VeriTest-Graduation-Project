module xor11 (
  input a,
  input b,
  input c,
  input d,
  output reg out
);

    always @(*) begin
        out = (^{a,b,c,d}); // XNOR using built-in operator
    end
    
    
endmodule
