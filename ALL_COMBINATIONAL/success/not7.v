module not7 (
  input in,
  output wire out
);

    reg temp;
    always @(*) begin
        temp = ~in; // Invert the input
    end
    
    assign out = temp;
    
endmodule