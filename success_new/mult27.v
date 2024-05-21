// wallace multiplier 4x4 - tested
module mult27(
    input [3:0] a,
    input [3:0] b,
    output [7:0] c
    );
	 wire [4:0]s1,d1,s,d;
	 wire v;
  //level 1
  assign c[0]=a[0]&b[0];
  // ha1
  assign c[1]=(a[0]&b[1])^(a[1]&b[0]);
  assign d[0]=(a[0]&b[1])&(a[1]&b[0]);

  // fa1
  assign s[0]=((a[0]&b[2])^(a[1]&b[1]))^(a[2]&b[0]);
  assign d[1]=((a[0]&b[2])&(a[1]&b[1]))|(a[1]&b[1]&(a[2]&b[0]))|((a[2]&b[0])&(a[0]&b[2]));

  // fa2
  assign s[1]=((a[0]&b[3])^(a[1]&b[2]))^(a[2]&b[1]);
  assign d[2]=((a[0]&b[3])&(a[1]&b[2]))|((a[1]&b[2])&(a[2]&b[1]))|((a[2]&b[1])&(a[0]&b[3]));

  // fa3
  assign s[2]=((a[1]&b[3])^(a[2]&b[2]))^(a[3]&b[1]);
  assign d[3]=((a[1]&b[3])&(a[2]&b[2]))|((a[2]&b[2])&(a[3]&b[1]))|((a[3]&b[1])&(a[1]&b[3]));

  // ha2
  assign s[3]=(a[2]&b[3])^(a[3]&b[2]);
  assign d[4]=(a[2]&b[3])&(a[3]&b[2]);
  //level 2
  // ha3
  assign c[2]=s[0]^d[0];
  assign d1[0]=s[0]&d[0];

  // fa4
  assign s1[0]=((a[3]&b[0])^s[1])^d[1];
  assign d1[1]=((a[3]&b[0])&s[1])|(s[1]&d[1])|(d[1]&(a[3]&b[0]));

  // ha4
  assign s1[1]=s[2]^d[2];
  assign d1[2]=s[2]&d[2];
  
  // ha5
  assign s1[2]=s[3]^d[3];
  assign d1[3]=s[3]&d[3];
  // ha6
  assign s1[3]=(a[3]&b[3])^d[4];
  assign d1[4]=(a[3]&b[3])&d[4];
  assign s1[4]=0;
  //level3 adder
   // adder 5
   wire [4:0]p,g,c1;
   assign p=s1^d1;
   assign g=s1&d1;
   assign c1[0]=0;
   assign c1[1]= g[0];
   assign c1[2]= g[1] | (p[1]&g[0]) ;
   assign c1[3]= g[2] | (p[2]&g[1]) | p[2]&p[1]&g[0] ;
   assign c1[4]= g[3] |  p[3]&g[2] | (p[3]&p[2]&g[1]) | p[3]&p[2]&p[1]&g[0] ;
   assign v= g[4]|p[4]&g[3] |  p[4]&p[3]&g[2] | (p[4]&p[3]&p[2]&g[1]) | p[4]&p[3]&p[2]&p[1]&g[0] ;
   assign c[7:3]=p^c1; 

endmodule
