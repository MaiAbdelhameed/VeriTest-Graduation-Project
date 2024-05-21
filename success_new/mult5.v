module mult5 (input [1:0]a,b,
            output reg [3:0] result); // tested

reg temp,temp2;

    always @(*) begin
      result[0] = a[0] & b[0];
      result[1] = (a[0] & b[1]) ^ (a[1] & b[0]);
      temp = ((a[1] & b[0]) & (a[0] & b[1]));
      temp2 = a[1] & b[1];
        result[2] = temp ^ temp2;
        result[3] = temp & temp2;       
    end
endmodule
