module xor_gate22 (
    input wire a,
    output out
);

    reg temp;
    always @(*) begin
        temp = ^a;
    end

    assign out = temp;
    
endmodule
