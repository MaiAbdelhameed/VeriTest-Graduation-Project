///4x2
module encoder37 (input [3:0] in, output [1:0] out);

    reg [1:0] temp;
    always @(*) begin
        if (in[3]) begin
            temp = 2'b11;
        end else if (in[2]) begin
            temp = 2'b10;
        end else if (in[1]) begin
            temp = 2'b01;
        end else begin
            temp = 2'b00;
        end
    end

    assign out = temp;

endmodule
