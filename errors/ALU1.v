module ALU1 (
  input [15:0] A,B,
  input [3:0] ALU_FUN,
  output reg Arith_Flag,
  output reg Logic_Flag,
  output reg CMP_Flag,
  output reg Shift_Flag,
  output reg [15:0] ALU_OUT
  );

  always @ (*)
  begin
    case (ALU_FUN)
      4'b0000: begin
        ALU_OUT=A+B;
        Arith_Flag=1;
        Logic_Flag=0;
        CMP_Flag=0;
        Shift_Flag=0;
      end
      4'b0001: begin
          ALU_OUT=A-B;
        Arith_Flag=1;
        Logic_Flag=0;
        CMP_Flag=0;
        Shift_Flag=0;
      end
      4'b0010: begin
        ALU_OUT=A*B;
        Arith_Flag=1;
        Logic_Flag=0;
        CMP_Flag=0;
        Shift_Flag=0;
      end
        4'b0011: begin
        ALU_OUT=A/B;
        Arith_Flag=1;
        Logic_Flag=0;
        CMP_Flag=0;
        Shift_Flag=0;
      end
        4'b0100: begin
        ALU_OUT=A&B;
        Arith_Flag=0;
        Logic_Flag=1;
        CMP_Flag=0;
        Shift_Flag=0; 
      end
      4'b0101: begin
        ALU_OUT=A|B;
        Arith_Flag=0;
        Logic_Flag=1;
        CMP_Flag=0;
        Shift_Flag=0; 
      end
      4'b0110: begin
        ALU_OUT=~(A&B);
        Arith_Flag=0;
        Logic_Flag=1;
        CMP_Flag=0;
        Shift_Flag=0; 
      end
      4'b0111: begin
        ALU_OUT=~(A|B);
        Arith_Flag=0;
        Logic_Flag=1;
        CMP_Flag=0;
        Shift_Flag=0; 
      end
      4'b1000: begin
        ALU_OUT=A^B;
        Arith_Flag=0;
        Logic_Flag=1;
        CMP_Flag=0;
        Shift_Flag=0; 
      end
      4'b1001: begin
        ALU_OUT=~(A^B);
        Arith_Flag=0;
        Logic_Flag=1;
        CMP_Flag=0;
        Shift_Flag=0; 
      end
      4'b1010: begin
         if(A==B)
           begin
             ALU_OUT='b0001;
           end
         else begin 
           ALU_OUT='b0000;
         end
        Arith_Flag=0;
        Logic_Flag=0;
        CMP_Flag=1;
        Shift_Flag=0; 
      end
      4'b1011: begin
         if(A>B)
           begin
             ALU_OUT='b0010;
           end
         else begin 
           ALU_OUT='b0000;
         end
        Arith_Flag=0;
        Logic_Flag=0;
        CMP_Flag=1;
        Shift_Flag=0; 
      end
      4'b1100: begin
         if(A<B)
           begin
             ALU_OUT='b0011;
           end
         else begin 
             ALU_OUT='b0000;
         end
        Arith_Flag=0;
        Logic_Flag=0;
        CMP_Flag=1;
        Shift_Flag=0; 
      end      
      4'b1101: begin
        ALU_OUT=A>>1;
        Arith_Flag=0;
        Logic_Flag=0;
        CMP_Flag=0;
        Shift_Flag=1;
      end
      4'b1110: begin
        ALU_OUT=A<<1;
        Arith_Flag=0;
        Logic_Flag=0;
        CMP_Flag=0;
        Shift_Flag=1;
      end
      default: begin ALU_OUT=0;
               Arith_Flag=0;
               Logic_Flag=0;
               CMP_Flag=0;
               Shift_Flag=0;
             end
    endcase
  end
endmodule

Error occurred: 'Divide' object has no attribute 'name'