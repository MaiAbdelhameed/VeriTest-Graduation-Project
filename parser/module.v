module mux_8x1 (h, h3, h2);


input [7:0] h;  
input [2:0] h3;     
output h2;

assign h2 = (h3 == 3'b000) ? h[0] :
                   (h3 == 3'b001) ? h[1] :
                   (h3 == 3'b010) ? h[2] :
                   (h3 == 3'b011) ? h[3] :
                   (h3 == 3'b100) ? h[4] :
                   (h3 == 3'b101) ? h[5] :
                   (h3 == 3'b110) ? h[6] :
                   			h[7];

endmodule