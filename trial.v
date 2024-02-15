//conditional expressions
module simple_or (
  input a,
  input b,
  output out
);

    always@(*) begin
      out = a | b;
    end

endmodule