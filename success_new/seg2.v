module seg2(
    bcd,
    seg
    );

    input [3:0] bcd; //initializing bcd as an 4 bit input signal
    output[7:0] seg; //initializing seg as an 8 bit output signal
    
    wire [7:0] seg; //initializing bcd signal as wires
    
    assign seg[0]= ((~bcd[3])&(~bcd[2])&(~bcd[1])&bcd[0]) | ((~bcd[3])&bcd[2]&(~bcd[1])&(~bcd[0])); //Logical expression for segment0 (Segment A)
    
    assign seg[1]= ((~bcd[3])&bcd[2]&(~bcd[1])&bcd[0]) | ((~bcd[3])&bcd[2]&bcd[1]&(~bcd[0])); //Logical expression for segment1 (Segment B)
    
    assign seg[2]= ((~bcd[3])&(~bcd[2])&bcd[1]&(~bcd[0])); //Logical expression for segment2 (Segment C)

    assign seg[3] = ((~bcd[3])&(~bcd[2])&(~bcd[1])&bcd[0]) | ((~bcd[3])&bcd[2]&(~bcd[1])&(~bcd[0])) | ((~bcd[3])&bcd[2]&bcd[1]&bcd[0]); //Logical expression for segment3 (Segment D)
    
    assign seg[4] = ((~bcd[3])&bcd[0]) | ((~bcd[3])&bcd[2]&(~bcd[1])) | (~(bcd[2])&(~bcd[1])&bcd[0]); //Logical expression for segment4 (Segment E)
    
    assign seg[5] = ((~bcd[3])&(~bcd[2])&bcd[0]) | ((~bcd[3])&(~bcd[2])&bcd[1]) | ((~bcd[3])&bcd[1]&bcd[0]); //Logical expression for segment5 (Segment F)
    
    assign seg[6] = ((~bcd[3])&(~bcd[2])&(~bcd[1]))|((~bcd[3])&bcd[2]&bcd[1]&bcd[0]); //Logical expression for segment6 (Segment G)
    
    assign seg[7] = 1; //Logical expression for segment7 (Segment Decimal Point)
    endmodule