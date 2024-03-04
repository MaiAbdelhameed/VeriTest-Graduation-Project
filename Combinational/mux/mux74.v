module mux74 (input in0, in1, sel,
                     output out);

    assign out = (sel== 1'b0) ? in0 : in1;

endmodule
