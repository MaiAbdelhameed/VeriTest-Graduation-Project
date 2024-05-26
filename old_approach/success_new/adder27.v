// brent kung 32 bits - tested - https://github.com/NamrathaCTR/32bit-Brent-Kung.git
module adder27(inputA,inputB,carryin,sum,carryOut);
input [31:0] inputA;
input [31:0] inputB;
input  carryin;
output [31:0] sum;
output  carryOut;
wire [31:0] POne;
wire [31:0] GOne;
parameter size=32;
reg [(size/2-1) :0] Ptwo;
reg [(size/2-1) :0] Gtwo;

reg [(size/4-1) :0] Pthree;
reg [(size/4-1) :0] Gthree;


reg [(size/8-1) :0] Gfour;
reg [(size/8-1) :0] Pfour;

reg [(size/16-1) :0] Gfive;
reg [(size/16-1) :0] Pfive;

wire Gsix;
wire Psix;


wire [32:1]C;



//loop
integer i;


assign POne=inputA ^ inputB;
assign GOne=inputA & inputB;

always@(POne,GOne)
begin
for(i=0;i<size/2 ;i=i+1)
begin
Gtwo[i]=GOne[{i,1'b0}+1'b1] | (POne[{i,1'b0}+1'b1]&GOne[{i,1'b0}]);
Ptwo[i]=(POne[{i,1'b0}])&POne[{i,1'b0}+1'b1];
end
end


always@(Gtwo,Ptwo)
begin
for(i=0;i<size/4 ;i=i+1)
begin
Gthree[i]=Gtwo[{i,1'b0}+1'b1] | (Ptwo[{i,1'b0}+1'b1]&Gtwo[{i,1'b0}]);
Pthree[i]=(Ptwo[{i,1'b0}])&Ptwo[{i,1'b0}+1'b1];
end
end

always@(Gthree,Pthree)
begin
for(i=0;i<size/8 ;i=i+1)
begin
Gfour[i]=Gthree[{i,1'b0}+1'b1] | (Pthree[{i,1'b0}+1'b1]&Gthree[{i,1'b0}]);
Pfour[i]=(Pthree[{i,1'b0}])&Pthree[{i,1'b0}+1'b1];
end
end

always@(Gfour,Pfour)
begin
for(i=0;i<size/16 ;i=i+1)
begin
Gfive[i ]=Gfour[{i,1'b0}+1'b1] | (Pfour[{i,1'b0}+1'b1]&Gfour[{i,1'b0}]);
Pfive[i]=(Pfour[{i,1'b0}])&Pfour[{i,1'b0}+1'b1];
end
end

assign Gsix=Gfive[1'b1] | (Gfive[1'b0] & Pfive[1'b1]);
assign Psix=Pfive[1'b1] & Pfive[1'b0];


assign C[1]=GOne[0] |(POne[0] & carryin);
assign C[2]=Gtwo[0] |(Ptwo[0] & carryin);
assign C[4]=Gthree[0] |(Pthree[0] & carryin);
assign C[8]=Gfour[0] |(Pfour[0] & carryin);
assign C[16]=Gfive[0] |(Pfive[0] & carryin);
assign C[32]=Gsix |(Psix & carryin);






assign C[3]=GOne[2] |(POne[2] & C[2]);
assign C[5]=GOne[4] |(POne[4] & C[4]);
assign C[7]=GOne[6] |(POne[6] & C[6]);
assign C[9]=GOne[8] |(POne[8] & C[8]);
assign C[11]=GOne[10] |(POne[10] & C[10]);
assign C[13]=GOne[12] |(POne[12] & C[12]);
assign C[15]=GOne[14] |(POne[14] & C[14]);
assign C[17]=GOne[16] |(POne[16] & C[16]);
assign C[19]=GOne[18] |(POne[18] & C[18]);
assign C[21]=GOne[20] |(POne[20] & C[20]);
assign C[23]=GOne[22] |(POne[22] & C[22]);
assign C[25]=GOne[24] |(POne[24] & C[24]);
assign C[27]=GOne[26] |(POne[26] & C[26]);
assign C[29]=GOne[28] |(POne[28] & C[28]);
assign C[31]=GOne[30] |(POne[30] & C[30]);




assign C[12]=Gthree[2] |(Pthree[2] & C[8]);
assign C[20]=Gthree[4] |(Pthree[4] & C[16]);
assign C[28]=Gthree[6] |(Pthree[6] & C[26]);




assign C[24]=Gfour[2] |(Pfour[2] & C[16]);




assign C[6]=Gtwo[2] |(Ptwo[2] & C[4]);
assign C[10]=Gtwo[4] |(Ptwo[4] & C[8]);
assign C[14]=Gtwo[6] |(Ptwo[6] & C[12]);
assign C[18]=Gtwo[8] |(Ptwo[8] & C[16]);
assign C[22]=Gtwo[10] |(Ptwo[10] & C[20]);
assign C[26]=Gtwo[12] |(Ptwo[12] & C[24]);
assign C[30]=Gtwo[14] |(Ptwo[14] & C[28]);





assign  sum= POne^ {C[31:1],carryin};
assign carryOut=C[32];




endmodule

/*
`timescale 10ns/1ps

module testBench;
reg [31:0] inputA;
reg [31:0] inputB;
reg carryin;
wire [31:0] sum;
wire  carryOut;

adder33 DUT(inputA,inputB,carryin,sum,carryOut);
initial 
begin
#5 inputA=32'h89028902; inputB=32'h11111111; carryin=1'b1;
#30 inputA=32'hffffffff; inputB=32'hffffffff; carryin=1'b1;
#30 inputA=32'hffff; inputB=32'h1111; carryin=1'b1;
#30 inputA=32'hffff; inputB=32'h1110; carryin=1'b0;


#100 $finish;
end

 
 initial begin 
    $dumpfile("dump.vcd"); $dumpvars;
  end
endmodule
*/