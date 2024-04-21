module decoder8 (ip0,ip1,ip2,op0,op1,op2,op3,op4,op5,op6,op7); // silicon vlsi 3-to-8 decoder

input ip0,ip1,ip2;
output reg op0,op1,op2,op3,op4,op5,op6,op7;

always @(*) begin
    case({ip2,ip1,ip0})
        3'b000: begin
            op0 = 1;
            {op1,op2,op3,op4,op5,op6,op7} = 7'd0;
        end            
        3'b001: begin
            op1 = 1;
            {op0,op2,op3,op4,op5,op6,op7} = 7'd0;
        end   
        3'b010: begin
            op2 = 1;
            {op0,op1,op3,op4,op5,op6,op7} = 7'd0;
        end   
        3'b011: begin
            op3 = 1;
            {op0,op1,op2,op4,op5,op6,op7} = 7'd0;
        end   
        3'b100: begin
            op4 = 1;
            {op0,op1,op2,op3,op5,op6,op7} = 7'd0;
        end   
        3'b101: begin
            op5 = 1;
            {op0,op1,op2,op3,op4,op6,op7} = 7'd0;
        end   
        3'b110: begin
            op6 = 1;
            {op0,op1,op2,op3,op4,op5,op7} = 7'd0;
        end   
        3'b111: begin
            op7 = 1;
            {op0,op1,op2,op3,op4,op5,op6} = 7'd0;
        end   
    endcase
end
endmodule
Error occurred: 'NoneType' object has no attribute 'name'