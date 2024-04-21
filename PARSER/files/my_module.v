// module test (input [1:0] a, input [1:0] b, output reg [3:0] c);

// reg  w1,w2;
// reg [1:0]w3;
// always @(*) begin
//    w1 = a[0] & b[0];
//    w2 = a[1] & b[1];
//    w3 = a & b;
//    c = {w1, w2,w3};
// end
// endmodule

// module and_gate6 (
//     input [1:0]a,
//     output wire out
// );

// assign out = (a == 2);

// endmodule


// module decoder17 (a,b,c,out);
// input a,b,c;
// output reg [7:0] out;

// always @(*)
// 	begin
//     case ({a,b,c})
//         3'b000: out=8'b0000_0001;
//         3'b001: out=8'b0000_0010;
//         3'b010: out=8'b0000_0100;
//         3'b011: out=8'b0000_1000;
//         3'b100: out=8'b0001_0000;
//         3'b101: out=8'b0010_0000;
//         3'b110: out=8'b0100_0000;
//         3'b111: out=8'b1000_0000;
//     endcase
//     end
// endmodule


module adder6(A,B,Cin,Sum,Cout);
    input A,B,Cin;
    output Sum,Cout;

    wire w1,w2,w3;

    xor x1 (w1,A,B);
    and A1 (w2,w1,Cin);
    xor X2 (Sum,w1,Cin);
    and A2 (w3,A,B);
    or O1 (Cout,w3,w2);
    
endmodule