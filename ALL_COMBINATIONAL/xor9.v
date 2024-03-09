module xor9 (
  input a,
  input b,
  output wire out
);

    reg temp;
    always @(*) begin
        temp = (a == b) ? 1'b0 : 1'b1; // Check if bits are equal
    end
    
    assign out = temp;
endmodule