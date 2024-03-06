//built-in operator
module or7 (
  input a,
  input b,
  output reg out
);
    always @(*) begin
        out = a | b;
    end
    
endmodule