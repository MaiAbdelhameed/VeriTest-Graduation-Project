// tested
module nor2_gate (
  input a,
  input b,
  output reg out
);

    always @(*) begin
        out = (~a && ~b) ? 1'b1 : 1'b0;
    end

    
endmodule
