// tested
module mux6 (input [3:0] a, b, input sel,
                    output [3:0] y);

    reg [3:0] temp_y;

    always @(*) begin
        if (sel)
            temp_y = b;
        else
            temp_y = a;
    end

    assign y = temp_y;

endmodule