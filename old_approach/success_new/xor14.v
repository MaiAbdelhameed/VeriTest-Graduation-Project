module xor14 (
  input a,
  input b,
  input c,
  input d,
  input e,
  input f,
  input g,
  output reg out
);

    always @(*) begin
        out = (^{a,b,c,d,e,f,g}); // XNOR using built-in operator
    end
    
    
endmodule
