module model2(
    input [2:0] IN,
    output OUT_AND,
    output OUT_OR
);

assign OUT_AND = IN[0] & IN[1] & IN[2];
assign OUT_OR = IN[0] | IN[1] | IN[2];

endmodule