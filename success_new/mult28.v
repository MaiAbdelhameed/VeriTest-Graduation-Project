// wallace multiplier 5x5 - tested
module mult28(
    input [4:0] A,
    input [4:0] B,
    output [9:0] Out
    );
    
    
    
    wire HA1_sum,HA2_sum,FA1_sum,FA2_sum,FA3_sum,FA4_sum;
    wire HA1_carry,HA2_carry,FA1_carry,FA2_carry,FA3_carry,FA4_carry;
    //Step-1
    assign {HA1_carry,HA1_sum} = (A[2]&B[0]) + (A[1]&B[1]);

    assign {FA1_carry,FA1_sum} = (A[3]&B[0]) + (A[2]&B[1]) + (A[1]&B[2]);
    assign {FA2_carry,FA2_sum} = (A[4]&B[0]) + (A[3]&B[1]) + (A[2]&B[2]);

    assign {HA2_carry,HA2_sum} = (A[1]&B[3]) + (A[0]&B[4]);

    assign {FA3_carry,FA3_sum} = (A[1]&B[4]) +  (A[4]&B[1]) + (A[3]&B[2]);
    assign {FA4_carry,FA4_sum} = (A[2]&B[4]) +  (A[3]&B[3]) + (A[4]&B[2]);   
    
    //Step-2
    wire HA_2_1_sum,FA_2_1_sum,FA_2_2_sum,HA_2_2_sum,FA_2_3_sum;
    wire HA_2_1_carry,FA_2_1_carry,FA_2_2_carry,HA_2_2_carry,FA_2_3_carry;
    
    assign {HA_2_1_carry,HA_2_1_sum} = FA1_sum+HA1_carry;
    assign {FA_2_1_carry,FA_2_1_sum} = (FA1_carry) + (FA2_sum  ) + (HA2_sum  );
    assign {FA_2_2_carry,FA_2_2_sum} = (FA3_sum  ) + (FA2_carry) + (HA2_carry);   
    assign {FA_2_3_carry,FA_2_3_sum} = (A[3]&B[4]) + (A[4]&B[3]) + (FA4_carry);
    
    assign {HA_2_2_carry,HA_2_2_sum} = FA4_sum+FA3_carry;//Checked
    
    
    //Step-3
    wire HA_3_1_sum, HA_3_2_sum, HA_3_3_sum, HA_3_4_sum;
    wire HA_3_1_carry, HA_3_2_carry, HA_3_3_carry, HA_3_4_carry;
    assign {HA_3_1_carry,HA_3_1_sum} = (FA_2_2_sum)+(FA_2_1_carry);
    assign {HA_3_2_carry,HA_3_2_sum} = (HA_2_2_sum)+(FA_2_2_carry);
    assign {HA_3_3_carry,HA_3_3_sum} = (FA_2_3_sum)+(HA_2_2_carry);
    assign {HA_3_4_carry,HA_3_4_sum} = (A[4]&B[4] )+(FA_2_3_carry);
    //Step-4 Final Addition Stage
    wire [9:0] arg1 = {1'b0,HA_3_4_sum,HA_3_3_sum,HA_3_2_sum,HA_3_1_sum,FA_2_1_sum,HA_2_1_sum,HA1_sum,A[1]&B[0],A[0]&B[0]};
    wire [9:0] arg2 = {HA_3_4_carry,HA_3_3_carry,HA_3_2_carry,HA_3_1_carry,A[2]&B[3],HA_2_1_carry,A[0]&B[3],A[0]&B[2],A[0]&B[1],1'b0};
    assign Out = arg1 + arg2;
    
    
endmodule
