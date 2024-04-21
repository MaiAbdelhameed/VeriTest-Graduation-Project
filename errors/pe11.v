module pe11 (i,en,y,v);
  // declare
    output reg v;
    input [7:0]i;
    input en;
  // store and declare output values
    output reg [2:0]y;
    always @(*)
    begin
        // priority encoder
        // if condition to choose 
        // output based on priority. 
        if(en == 1) begin
        if(i[7]==1) {y,v}=4'b1111;
        else if(i[6]==1) {y,v}=4'b1101;
        else if(i[5]==1) {y,v}=4'b1011;
        else if(i[4]==1) {y,v}=4'b1001;
        else if(i[3]==1) {y,v}=4'b0111;
        else if(i[2]==1) {y,v}=4'b0101;
        else if(i[1]==1) {y,v}=4'b0011;
        else
        {y,v}=4'b0000;
        end
        else
            {y,v}=4'b0000;
    end
endmodule
Error occurred: 'NoneType' object has no attribute 'connections'