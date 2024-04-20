module encoder20 (a0,a1,a2,a3,en,y0,y1);
    input a0,a1,a2,a3;
    input en;
    output reg y0,y1;
    
    always@(*)
    begin
        if(!en) begin
            y0 =1'b0;
            y1 = 1'b0;
        end
        else
        case({a3,a2,a1,a0})
            4'b0001:
                begin 
                    y0= 1'b0;
                    y1 = 1'b0; 
                end
            4'b0010:
                begin 
                    y0= 1'b1;
                    y1 = 1'b0; 
                end
            4'b0100: 
                begin 
                    y0= 1'b0;
                    y1 = 1'b1; 
                end
            4'b1000:
                begin 
                    y0= 1'b1;
                    y1 = 1'b1;  
                end
            default: begin
                y0= 1'b0;
                y1 = 1'b0; 
            end 
        endcase
    end
endmodule