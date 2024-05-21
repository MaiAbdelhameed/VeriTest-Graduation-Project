module decoder19 (in,out3);

    output reg [7:0] out3;
    input [2:0] in;
    always @(in) begin
    out3 = 8'b0000_0001 << in;
    end


endmodule