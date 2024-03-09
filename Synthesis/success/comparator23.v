module comparator23 (input a, input b, output eq, output gt, output lt);

    reg temp1, temp2, temp3;

    always @(*) begin
        temp1 = (a == b);
        temp2 = (a > b);
        temp3 = (a < b);
    end
    
    assign eq = temp1;
    assign gt = temp2;
    assign lt = temp3;
endmodule
