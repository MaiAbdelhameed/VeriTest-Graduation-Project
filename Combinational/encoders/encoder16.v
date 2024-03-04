module encoder16 (D0,D1,D2,D3,D4,D5,D6,D7,
y0,y1,y2);

input D0,D1,D2,D3,D4,D5,D6,D7;
output y0,y1,y2;

assign y2 = D4 | D5 | D6 | D7;
assign y1 = D2 | D3 | D6 | D7;
assign y0 = D1 | D3 | D5 | D7;
endmodule