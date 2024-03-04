module sub12 (A, B, Diff, Borrow);
input A, B;
output reg Diff, Borrow;
always @ (*)
begin
case ({A, B})
3'b00: Diff = 0;
3'b01: Diff = 1;
3'b10: Diff = 1;
3'b11: Diff = 0;
endcase
case ({A, B})
3'b00: Borrow = 0;
3'b01: Borrow = 1;
3'b10: Borrow = 0;
3'b11: Borrow = 0;
endcase
end
endmodule