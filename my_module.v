module adder11(A, B, Cin, Sum, Cout);
    input A, B, Cin;
    output reg Sum, Cout;

    always @(*) begin
        if (A == 1'b0 && B == 1'b0 && Cin == 1'b0) begin
            Sum = 1'b0;
            Cout = 1'b0;
        end
        else if (A == 1'b0 && B == 1'b0 && Cin == 1'b1) begin
            Sum = 1'b1;
            Cout = 1'b0;
        end
        else if (A == 1'b0 && B == 1'b1 && Cin == 1'b0) begin
            Sum = 1'b1;
            Cout = 1'b0;
        end
        else if (A == 1'b0 && B == 1'b1 && Cin == 1'b1) begin
            Sum = 1'b0;
            Cout = 1'b1;
        end
        else if (A == 1'b1 && B == 1'b0 && Cin == 1'b0) begin
            Sum = 1'b1;
            Cout = 1'b0;
        end
        else if (A == 1'b1 && B == 1'b0 && Cin == 1'b1) begin
            Sum = 1'b0;
            Cout = 1'b1;
        end
        else if (A == 1'b1 && B == 1'b1 && Cin == 1'b0) begin
            Sum = 1'b0;
            Cout = 1'b1;
        end
        else if (A == 1'b1 && B == 1'b1 && Cin == 1'b1) begin
            Sum = 1'b1;
            Cout = 1'b1;
        end
    end
endmodule
