// array multiplier 4x4 
module mult24(a,b,out); //tested
input [3:0]a,b;       // 4 bit a and b to be multiplied
output [7:0]out;      // multiplication output 
wire [3:0]w1,w2,w3,w4,s1,s2;  // wires for inter connection


and(out[0],a[0],b[0]);
and(w1[1],a[0],b[1]);
and(w1[2],a[0],b[2]);
and(w1[3],a[0],b[3]);

and(w2[0],a[1],b[0]);
and(w2[1],a[1],b[1]);
and(w2[2],a[1],b[2]);
and(w2[3],a[1],b[3]);

and(w3[0],a[2],b[0]);
and(w3[1],a[2],b[1]);
and(w3[2],a[2],b[2]);
and(w3[3],a[2],b[3]);

and(w4[0],a[3],b[0]);
and(w4[1],a[3],b[1]);
and(w4[2],a[3],b[2]);
and(w4[3],a[3],b[3]);

assign {s1[3],{s1[2],s1[1],s1[0],out[1]}} = {0,w1[3],w1[2],w1[1]} + {w2[3],w2[2],w2[1],w2[0]};

assign {s2[3],{s2[2],s2[1],s2[0],out[2]}} = {s1[3],s1[2],s1[1],s1[0]} + {w3[3],w3[2],w3[1],w3[0]};

assign {out[7],{out[6],out[5],out[4],out[3]}} = {s2[3],s2[2],s2[1],s2[0]}+{w4[3],w4[2],w4[1],w4[0]};

endmodule