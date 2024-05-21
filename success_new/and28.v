// 5 input and
// tested
module and28 (
  input a,
  input b,
  input c,
  input d,
  input e,
  output out
);

  assign out = &{a,b,c,d,e}; // Performs an AND operation

endmodule
