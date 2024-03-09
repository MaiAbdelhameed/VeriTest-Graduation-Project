module mux64 (input [15:0] in,
                                input [3:0] sel,
                                output  out);

    reg temp;
    always @* begin
        case(sel)
            4'b0000: temp = in[0];
            4'b0001: temp = in[1];
            4'b0010: temp = in[2];
            4'b0011: temp = in[3];
            4'b0100: temp = in[4];
            4'b0101: temp = in[5];
            4'b0110: temp = in[6];
            4'b0111: temp = in[7];
            4'b1000: temp = in[8];
            4'b1001: temp = in[9];
            4'b1010: temp = in[10];
            4'b1011: temp = in[11];
            4'b1100: temp = in[12];
            4'b1101: temp = in[13];
            4'b1110: temp = in[14];
            4'b1111: temp = in[15];
        endcase
    end

    assign out = temp;

endmodule
