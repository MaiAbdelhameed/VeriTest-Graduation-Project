module nor7 (
  input a,
  input b,
  output out
);

    reg temp;
    always @(*) begin
        temp = ~(a | b); // NOR using built-in operator
    end

    assign out = temp;
    
endmodule