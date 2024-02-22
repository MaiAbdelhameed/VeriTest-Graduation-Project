// module mux4x1_dataflow_kmap(input [3:0] a, b, c, d,
//                              input [1:0] sel,
//                              output y);

//     assign y[0] = (sel == 2'b00) ? a[0] : (sel == 2'b01) ? b[0] : (sel == 2'b10) ? c[0] : d[0];
//     assign y[1] = (sel == 2'b00) ? a[1] : (sel == 2'b01) ? b[1] : (sel == 2'b10) ? c[1] : d[1];
//     assign y[2] = (sel == 2'b00) ? a[2] : (sel == 2'b01) ? b[2] : (sel == 2'b10) ? c[2] : d[2];
//     assign y[3] = (sel == 2'b00) ? a[3] : (sel == 2'b01) ? b[3] : (sel == 2'b10) ? c[3] : d[3];


// endmodule