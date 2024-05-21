module xor13 (
  input a,
  input b,
  input c,
  input d,
  input e,
  input f,
  output reg out
);

    always @(*) begin
        out = (^{a,b,c,d,e,f}); // XNOR using built-in operator
    end
    
    
endmodule
