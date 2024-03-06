module mux5 (input in0, in1, sel,
                    output out);

    assign out = (sel== 1'b0) ? in0 : (sel == 1'b1) ? in1: out;

endmodule