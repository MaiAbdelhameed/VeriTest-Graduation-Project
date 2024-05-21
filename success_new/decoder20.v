module decoder20 (in,out3);

    output reg [7:0] out3;
    input [1:0] in;
    always @(in) begin
    out3 = 4'b0001 << in;
    end


endmodule