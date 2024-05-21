// koggestone 4 bits - tested
module adder26(a,b,s,cin,cout);    //MANOJ KUMAR.CM
input [3:0]a,b;
input cin;
output [3:0]s;
output cout;
wire [3:0]p,g,P,G,PP,GG;
assign p=a^b;assign g=a&b;
assign P[0]=p[0];
assign G[0]=g[0];
assign P[1]=p[1]&p[0];
assign G[1]=(p[1]&g[0])|g[1];
assign P[2]=p[2]&p[1];
assign G[2]=(p[2]&g[1])|g[2];
assign P[3]=p[3]&p[2];
assign G[3]=(p[3]&g[2])|g[3];
assign PP[0]=P[0];
assign GG[0]=G[0];
assign PP[1]=P[1];
assign GG[1]=G[1];
assign PP[2]=P[2]&P[0];
assign GG[2]=(P[2]&G[0])|G[2];
assign PP[3]=P[3]&P[1];
assign GG[3]=(P[3]&G[1])|G[3];
assign s[0]=p[0]^cin;
assign s[1]=p[1]^GG[0];
assign s[2]=p[2]^GG[1];
assign s[3]=p[3]^GG[2];
assign cout=GG[3];
endmodule


