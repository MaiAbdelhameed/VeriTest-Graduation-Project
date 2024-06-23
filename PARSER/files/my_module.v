module coverage(
  a,b,c, d, k
);

input[2:0] a,b;
output[1:0] k;


always @ * begin


if (a == b)
  begin
  if (a<1)
    k = 2'b00;
  else
    if (a == 2)
      k = 2'b01;
    else
      if (a == 3)
        k = 2'b11;
      else
        k = 2'b10;
  end
  






end
endmodule
