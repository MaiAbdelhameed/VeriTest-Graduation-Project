module encoder8 (y1,y2,y3,a0,a1);
    input y1,y2,y3;
    output a0,a1;

    assign a0 = y3 | y1;
    assign a1 = y3 | y2;

endmodule