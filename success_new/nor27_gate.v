// tested
module nor27_gate (
  input a,
  input b,
  input c,
  input d,
  input e,
  input f,
  output wire out
);

  assign out = ~(|{a,b,c,d,e,f});

endmodule
