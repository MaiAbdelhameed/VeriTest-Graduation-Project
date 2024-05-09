module xor6 (
  input a,
  input b,
  output reg out
);

    always @(*) begin
        out = a ^ b; // ^ represents the XOR operator
    end
    
endmodule