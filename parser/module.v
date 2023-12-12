module IfElseExample (
  input a,
  input b,
  output [3:0] result
);


  assign result[2:0] = a & b;

  always @* begin
    // If-Else condition
    if (a & b) begin
      // If 'a' and 'b' are both true
      result = 1;
    end
    else if (a ^ b) begin

      result = 2;
      
    end
    else begin
      // If either 'a' or 'b' is false
      result = 0;
    end
  end

endmodule
