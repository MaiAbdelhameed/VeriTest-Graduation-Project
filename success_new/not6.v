module not6 (
  input in,
  output reg out
);

    always @(*) begin
        out = ~in; // Invert the input
    end
    
endmodule