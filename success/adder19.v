module adder19(A,B,Sum,Cout);
    input A,B;
    output reg Sum,Cout;

    always @(*) begin
        case({A,B})
            2'b00: begin
                Sum = 0;
                Cout = 0;
            end
            2'b01: begin
                Sum = 1;
                Cout = 0;
            end
            2'b10: begin
                Sum = 1;
                Cout = 0;
            end
            2'b11: begin
                Sum = 0;
                Cout = 1;
            end
        endcase
    end
endmodule