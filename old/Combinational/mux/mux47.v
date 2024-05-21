module mux47 (input in0, in1,in2,in3, sel,
                     output out);

    assign out = (sel == 2'b00) ? in0 : (sel == 2'b01) ? in1 : (sel == 2'b10)  ? in2 :  (sel == 2'b11) ? in3: 4'b0000;

endmodule
