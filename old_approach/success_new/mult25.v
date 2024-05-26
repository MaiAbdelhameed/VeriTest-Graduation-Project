// array multiplier 2x2 - tested
module mult25(
input [1:0]x,
input [1:0]y,
output [3:0]out
);
wire p0,p1,p2,c1;
and(out[0], x[0],y[0]);
and(p0,x[1],y[0]);
and(p1,x[0],y[1]);
and(p2,x[1],y[1]);

assign {c1,out[1]} = p0 + p1;

assign {out[3],out[2]} = p2 + c1;
endmodule