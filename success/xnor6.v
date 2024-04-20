module xnor6 (
  input a,
  input b,
  output reg out
);

    always @(*) begin
        out = a ^ ~b; // XNOR using built-in operator
    end
    
endmodule
