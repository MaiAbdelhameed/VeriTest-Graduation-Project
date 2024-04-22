module xnor7 (
  input a,
  input b,
  output wire out
);

    reg temp;
    always @(*) begin
        temp = a ^ ~b; // XNOR using built-in operator
    end
    
    assign out = temp;
    
endmodule
