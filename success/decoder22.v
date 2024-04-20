module decoder22 (a,b,c,en,d0,d1,d2,d3,d4,d5,d6,d7);
input a,b,c,en;
output d0,d1,d2,d3,d4,d5,d6,d7;
assign d0=(en&~a&~b&~c);
assign d1=(en&~a&~b&c);
assign d2=(en&~a&b&~c);
assign d3=(en&~a&b&c);
assign d4=(en&a&~b&~c);
assign d5=(en&a&~b&c);
assign d6=(en&a&b&~c);
assign d7=(en&a&b&c);
endmodule