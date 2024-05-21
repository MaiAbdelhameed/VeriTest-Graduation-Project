module encoder19 (en,D1,D2,D3,D4,D5,D6,D7,
y0,y1,y2);

input en,D1,D2,D3,D4,D5,D6,D7;
output y0,y1,y2;

assign y2 = en & (D4 | D5 | D6 | D7);
assign y1 = en & (D2 | D3 | D6 | D7);
assign y0 = en & (D1 | D3 | D5 | D7);
endmodule