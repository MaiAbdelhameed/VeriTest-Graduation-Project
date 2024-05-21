module xnor13 (
  input a,
  input b,
  input c,
  input d,
  input e,
  input f,
  input g,
  input h,
  output reg out
);

    always @(*) begin
        out = ~(^{a,b,c,d,e,f,g,h}); // XNOR using built-in operator
    end
    
    
endmodule
