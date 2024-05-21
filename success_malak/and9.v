// tested
module and9 (
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