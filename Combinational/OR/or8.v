//built-in operator
module or8 (
  input a,
  input b,
  output out
);

    reg temp;
    always @(*) begin:
        temp = a | b;
    end
    
    assign out = temp;
endmodule