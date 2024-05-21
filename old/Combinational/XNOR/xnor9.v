module xnor9 (
  input a,
  input b,
  output wire out
);

    reg temp;
    always @(*) begin
        temp = (a == b) ? 1'b1 : 1'b0; // XNOR using conditional expression (XOR and invert both)
    end
    
    assign out = temp;
endmodule
