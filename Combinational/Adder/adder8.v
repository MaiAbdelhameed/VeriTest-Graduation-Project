module adder8 (A, B, S, C);
    input A, B;
    output reg S, C;

    always @ (*)
    begin
        if (A == 1'b0 && B == 1'b0) begin
            S = 1'b0;
            C = 1'b0;
        end
        else if (A == 1'b0 && B == 1'b1) begin
            S = 1'b1;
            C = 1'b0;
        end
        else if (A == 1'b1 && B == 1'b0) begin
            S = 1'b1;
            C = 1'b0;
        end
        else if (A == 1'b1 && B == 1'b1) begin
            S = 1'b0;
            C = 1'b1;
        end
    end
endmodule
