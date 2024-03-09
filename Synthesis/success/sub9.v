module sub9 (input a, b, Bin, output D, Bout);
    assign D = a ^ b ^ Bin;
    assign Bout = (~a & b) | (~(a ^ b) & Bin);
endmodule