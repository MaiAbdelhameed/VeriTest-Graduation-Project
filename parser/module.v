module mux_4to_assign (a,b,c,d,sel,out);

input [3:0] a;

input [3:0] b; 
input [3:0] c; 

input [3:0] d; 

input [1:0] sel; 
output [2:0] out; 


assign out = (a[2:0] & c[2:0]) | a[2:0];

endmodule
