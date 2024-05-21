// carry select adder 4 bits - tested
module adder19
        (   input [3:0] A,B,
            input cin,
            output reg [3:0] S,
            output reg cout
            );
        

wire [3:0] temp0,temp1,carry0,carry1;

// -- for carry 0
// full adder 00
assign temp0[0] = A[0] ^ B[0] ^ 1'b0;
assign carry0[0] = (A[0] & B[0]) | (1'b0 & B[0]) | (A[0] & 1'b0);
// full adder 01
assign temp0[1] = A[1] ^ B[1] ^ carry0[0];
assign carry0[1] = (A[1] & B[1]) | (carry0[0] & B[1]) | (A[1] & carry0[0]);
// full adder 02
assign temp0[2] = A[2] ^ B[2] ^ carry0[1];
assign carry0[2] = (A[2] & B[2]) | (carry0[1] & B[2]) | (A[2] & carry0[1]);
// full adder 03
assign temp0[3] = A[3] ^ B[3] ^ carry0[2];
assign carry0[3] = (A[3] & B[3]) | (carry0[2] & B[3]) | (A[3] & carry0[2]);

// -- for carry 1
// full adder 10
assign temp1[0] = A[0] ^ B[0] ^ 1'b1;
assign carry1[0] = (A[0] & B[0]) | (1'b1 & B[0]) | (A[0] & 1'b1);
// full adder 11
assign temp1[1] = A[1] ^ B[1] ^ carry1[0];
assign carry1[1] = (A[1] & B[1]) | (carry1[0] & B[1]) | (A[1] & carry1[0]);
// full adder 12
assign temp1[2] = A[2] ^ B[2] ^ carry1[1];
assign carry1[2] = (A[2] & B[2]) | (carry1[1] & B[2]) | (A[2] & carry1[1]);
// full adder 13
assign temp1[3] = A[3] ^ B[3] ^ carry1[2];
assign carry1[3] = (A[3] & B[3]) | (carry1[2] & B[3]) | (A[3] & carry1[2]);

always@(*)
begin
// mux carry
if(cin == 0)
    cout = carry0[3];
else
    cout = carry1[3]; 

// mux sum0
if(cin == 0)
    S[0] = temp0[0];
else
    S[0] = temp1[0]; 

// mux sum1
if(cin == 0)
    S[1] = temp0[1];
else
    S[1] = temp1[1]; 

// mux sum2
if(cin == 0)
    S[2] = temp0[2];
else
    S[2] = temp1[2];  

// mux sum3
if(cin == 0)
    S[3] = temp0[3];
else
    S[3] = temp1[3]; 
end

endmodule 