module nor9 (
  input a,
  input b,
  output wire out
);

    reg temp;
    always @(*) begin
        temp = (a == 1'b1 && b == 1'b1) ? 1'b0 : 1'b1; // NOR using conditional expression
    end

    assign out = temp;
    
endmodule
