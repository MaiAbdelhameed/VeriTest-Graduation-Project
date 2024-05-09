module comparator1 (a,b,z,n,v);
input [3:0] a,b;
output z,n,v;

wire [3:0] s;
wire cout;

wire c1,c2,c3;

assign s[0] = a[0] ^ ~b[0] ^ 1;
assign c1 = ( ~b[0] & a[0] ) | (1 & ( a[0] ^ ~b[0] ));

assign s[1] = a[1] ^ ~b[1] ^ c1;
assign c2 = ( ~b[1] & a[1] ) | (c1 & ( a[1] ^ ~b[1] ));

assign s[2] = a[2] ^ ~b[2] ^ c2;
assign c3 = ( ~b[2] & a[2] ) | (c2 & ( a[2] ^ ~b[2] ));

assign s[3] = a[3] ^ ~b[3] ^ c3;
assign cout = ( ~b[3] & a[3] ) | (c3 & ( a[3] ^ ~b[3] ));

assign z = ~(s[0] | s[1] | s[2] | s[3]);

assign n = s[3];

assign v = cout ^ c3;
endmodule
