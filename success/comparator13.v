module comparator13 (input A0,A1,B0,B1, output A_less_B, A_equal_B, A_greater_B);  
wire tmp1,tmp2,tmp3,tmp4,tmp5, tmp6, tmp7, tmp8;  
// A = B output   
xnor u1(tmp1,A1,B1);  
xnor u2(tmp2,A0,B0);  
and u3(A_equal_B,tmp1,tmp2);  
// A less than B output   
assign tmp3 = (~A0)& (~A1)& B0;  
assign tmp4 = (~A1)& B1;  
assign tmp5 = (~A0)& B1& B0;  
assign A_less_B = tmp3 | tmp4 | tmp5;  
// A greater than B output   
assign tmp6 = (~B0)& (~B1)& A0;  
assign tmp7 = (~B1)& A1;  
assign tmp8 = (~B0)& A1& A0;  
assign A_greater_B = tmp6 | tmp7 | tmp8;  
endmodule