module xor_gate7 (
  input a,
  input b,
  output out
);

    reg temp;
    always @(*) begin
        temp = a ^ b; // ^ represents the XOR operator
    end
    
    assign out = temp;
endmodule