module xor12 (
  input a,
  input b,
  input c,
  input d,
  input e,
  output reg out
);

    always @(*) begin
        out = (^{a,b,c,d,e}); // XNOR using built-in operator
    end
    
    
endmodule
