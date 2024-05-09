module adder12 (A, B, S, C);
input A, B;
output reg S, C;
always @ (*)
begin
    case ({A, B})
        2'b00: S = 0;
        2'b01: S = 1;
        2'b10: S = 1;
        2'b11: S = 0;
    endcase
    case ({A, B})
        2'b00: C = 0;
        2'b01: C = 0;
        2'b10: C = 0;
        2'b11: C = 1;
    endcase
end
endmodule
