module NestedIfExample (
    input wire condition_1,
    input wire condition_2,
    output reg result
);

    always @(*) begin
        if (condition_1 == 1) begin
            if (condition_2 == 1) begin
                result = 1; // Both conditions are true
            end
            else begin
                result = 2; // Only condition_1 is true
            end
        end
        else begin
            if (condition_2 == 1) begin
                result = 3; // Only condition_2 is true
            end
            else begin
                result = 4; // Neither condition is true
            end
        end
    end

endmodule
