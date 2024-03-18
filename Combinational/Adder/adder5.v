module adder5(A,B,Cin,Sum,Cout);

    input A,B,Cin;
    output reg Sum,Cout;

    always @(*) begin
        case({A,B,Cin}) begin
            3'b000: begin
                Sum = 1'b0;
                Cout = 1'b0;
            end
            3'b001: begin
                Sum = 1'b1;
                Cout = 1'b0;
            end
            3'b010: begin
                Sum = 1'b1;
                Cout = 1'b0;
            end
            3'b011: begin
                Sum = 1'b0;
                Cout = 1'b1;
            end
            3'b100: begin
                Sum = 1'b1;
                Cout = 1'b0;
            end
            3'b101: begin
                Sum = 1'b0;
                Cout = 1'b1;
            end
            3'b110: begin
                Sum = 1'b0;
                Cout = 1'b1;
            end
            3'b111: begin
                Sum = 1'b1;
                Cout = 1'b1;
            end
        end
        endcase
    end
endmodule