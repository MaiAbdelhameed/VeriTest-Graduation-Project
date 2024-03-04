module xor7 (
  input a,
  input b,
  output reg out
);

    reg temp;
    always @(*) begin:
        temp = a ^ b; // ^ represents the XOR operator
    end
    
    assign out = temp;
endmodule