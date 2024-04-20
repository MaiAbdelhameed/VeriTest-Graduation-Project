module sub7 (A,B,Bin,D,Bout);
    input A,B,Bin;
    output reg D,Bout;

    always @(*) begin
        case ({A,B,Bin})
            3'b000: begin
                D = 1'b0;
                Bout = 1'b0;
            end 
            3'b001: begin
                D = 1'b1;
                Bout = 1'b1;
            end 
            3'b010: begin
                D = 1'b1;
                Bout = 1'b1;
            end 
            3'b011: begin
                D = 1'b0;
                Bout = 1'b1;
            end 
            3'b100: begin
                D = 1'b1;
                Bout = 1'b0;
            end 
            3'b101: begin
                D = 1'b0;
                Bout = 1'b0;
            end 
            3'b110: begin
                D = 1'b0;
                Bout = 1'b0;
            end
            3'b111: begin
                D = 1'b1;
                Bout = 1'b1;
            end
        endcase
    end
endmodule