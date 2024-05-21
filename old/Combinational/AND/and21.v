module and21 (
    input wire a,
    output wire out
);

    reg temp;
    always @(*) begin
        temp = &{a};
    end

    assign out = temp;
endmodule
