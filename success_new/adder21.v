// carry look ahead adder 4 bits - tested
module adder21(S,Cout,a,b,Cin);
input [3:0]a,b;
input Cin;
output [3:0]S;
output Cout;
wire [3:0]g,p;
wire w1,w2,w3,w4;
assign p[0] = a[0]^b[0];assign p[1] = a[1]^b[1];
assign p[2] = a[2]^b[2];assign p[3] = a[3]^b[3];
assign g[0] = a[0]&b[0];assign g[1] = a[1]&b[1];
assign g[2] = a[2]&b[2];assign g[3] = a[3]&b[3];
assign w1 = g[0]|(Cin&p[0]);
assign w2 = g[1]|(w1&p[1]);
assign w3 = g[2]|(w2&p[2]);
assign w4 = g[3]|(w3&p[3]);
assign Cout = w4; assign S[0] = p[0]^Cin;
assign S[1] = p[1]^w1; assign S[2] = p[2]^w2;
assign S[3] = p[3]^w3;
endmodule