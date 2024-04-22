module not12 (
  input in,
  output wire out
);


    reg temp;
    always @(*) begin
        case (in)
            1'b0: temp = 1'b1;
            default: temp = 1'b0;
        endcase
    end

    assign out = temp;
endmodule