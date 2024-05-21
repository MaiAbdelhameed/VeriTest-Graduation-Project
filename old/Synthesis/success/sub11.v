module sub11 (A,B,D,Bout);

    input A,B;
    output reg D,Bout;

    always @(*) begin
        case({A,B})
            2'b00: begin
                D = 0;
                Bout = 0;
            end
            2'b01: begin
                D = 1;
                Bout = 1;
            end
            2'b10: begin
                D = 1;
                Bout = 0;
            end
            2'b11: begin
                D = 0;
                Bout = 0;
            end
        endcase
    end
endmodule