module primitive_comparator (
  input [WIDTH-1:0] a,
  input [WIDTH-1:0] b,
  output reg eq,
  output reg greater,
  output reg less
);

  always @(*) begin
    comparator #(WIDTH) comp_inst (.a(a), .b(b), .eq(eq), .gt(greater), .lt(less));
  end

endmodule
