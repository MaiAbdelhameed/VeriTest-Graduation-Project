module mux76 (input [3:0] in0, in1, in2, in3,
                     input [1:0] sel,
                     output reg out);

    always @* begin
        case(sel)
            2'b00: out = in0;
            2'b01: out = in1;
            2'b10: out = in2;
            default: out = in3;
        endcase
    end

endmodule

Error occurred:  line:10: before: "out"