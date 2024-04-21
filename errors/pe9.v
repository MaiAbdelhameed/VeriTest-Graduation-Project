module pe9 (D0,D1,D2,D3,Y1,Y0,V);

    input D0,D1,D2,D3;
    output reg Y1,Y0,V;

    always @(*) begin
        if(D3 == 1) {Y1,Y0,V} = 3'b111;
        else if(D2 == 1) {Y1,Y0,V} = 3'b101;
        else if(D1 == 1) {Y1,Y0,V} = 3'b011;
        else if(D0 == 1) {Y1,Y0,V} = 3'b001;
        else {Y1,Y0,V} = 3'b000;
    end

endmodule
Error occurred: 'NoneType' object has no attribute 'connections'