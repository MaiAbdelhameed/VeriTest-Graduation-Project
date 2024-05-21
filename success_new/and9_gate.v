// tested
module and9_gate (
  input a,
  input b,
  output reg out
);

    always @(*) begin
        if(a == 0)
            out = 0;
        else
            out = 1;

        if(b == 0)
            out = 0;

    end

endmodule