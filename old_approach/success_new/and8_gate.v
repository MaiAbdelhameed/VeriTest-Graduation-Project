// tested
module and8_gate (
  input a,
  input b,
  output reg out
);

    always @(*) begin
        if(a == 0)
            out = 0;
        else begin
            if(b == 0)
                out = 0;
            else
                out = 1;
        end

    end

endmodule