// tested
module xor3 (
  input a,
  input b,
  output reg out
);

    always @(*) begin
        out = (a ^ b) ? 1'b1 : 1'b0; // Check if bits are equal
    end
    
endmodule