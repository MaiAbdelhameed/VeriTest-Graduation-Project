module encoder11 (y1,y2,y3,a0,a1,en);
    input y1,y2,y3,en;
    output a0,a1;

    assign a0 = en & (y3 | y1);
    assign a1 = en & (y3 | y2);

endmodule