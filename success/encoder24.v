module encoder24 (a,y); // Test
    input [15:0] a;
    output reg [3:0] y;
    always@(a)
    begin
        case(a)
            16'b0000_0000_0000_0001:y=4'b0000;
            16'b0000_0000_0000_0010:y=4'b0001;
            16'b0000_0000_0000_0100:y=4'b0010;
            16'b0000_0000_0000_1000:y=4'b0011;
            16'b0000_0000_0001_0000:y=4'b0100;
            16'b0000_0000_0010_0000:y=4'b0101;
            16'b0000_0000_0100_0000:y=4'b0110;
            16'b0000_0000_1000_0000:y=4'b0111;
            16'b0000_0001_0000_0000:y=4'b1000;
            16'b0000_0010_0000_0000:y=4'b1001;
            16'b0000_0100_0000_0000:y=4'b1010;
            16'b0000_1000_0000_0000:y=4'b1011;
            16'b0001_0000_0000_0000:y=4'b1100;
            16'b0010_0000_0000_0000:y=4'b1101;
            16'b0100_0000_0000_0000:y=4'b1110;
            16'b1000_0000_0000_0000:y=4'b1111;
            default: y = 4'b0000; 
        endcase
    end
endmodule