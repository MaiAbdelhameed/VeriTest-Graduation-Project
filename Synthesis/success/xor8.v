module xor8 (
  input a,
  input b,
  output reg out
);

    always @(*) begin
        out = (a == b) ? 1'b0 : 1'b1; // Check if bits are equal
    end
    
endmodule