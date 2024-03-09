module decoder29 (x,y,z,w,d);
input  w,x,y,z;
output [15:0]d;
assign d[0]=  (~x) & (~y) &(~z) & (~w)  ;
assign d[1]=  (~x) & (~y) &(~z) & (w) ;
assign d[2]=  (~x) & (~y) &(z) & (~w) ;
assign d[3]=  (~x) & (~y) &(z)  & (w) ;
assign d[4]=  (~x) & (y) &(~z) & (~w) ;
assign d[5]=  (~x) & (y) &(~z)  & (w) ;
assign d[6]=  (~x) & (y) &(z)  & (~w) ;
assign d[7]=  (~x) & (y) &(z)  & (w) ; 
assign d[8]=  (x) & (~y) &(~z) & (~w) ;
assign d[9]=  (x) & (~y) &(~z) & (w) ; 
assign d[10]= (x) & (~y) &(z) & (~w) ; 
assign d[11]= (x) & (~y) &(z)  & (w) ; 
assign d[12]= (x) & (y) &(~z) & (~w) ; 
assign d[13]= (x) & (y) &(~z)  & (w) ; 
assign d[14]= (x) & (y) &(z)  & (~w) ; 
assign d[15]= (x) & (y) &(z)  & (w) ;

endmodule