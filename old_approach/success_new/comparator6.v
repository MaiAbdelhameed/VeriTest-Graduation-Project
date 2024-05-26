module comparator6 (A,B,C,D,E);

	input [3:0]A;
	input [3:0]B;
	output reg C,D,E;

	always@(*) begin

	if(A>B) begin
        E = 1;
        C = 0;
        D = 0;
    end
	else if(A<B) begin
        C = 1;
        D = 0;
        E = 0;
    end
	else begin
        D = 1;
        C = 0;
        E = 0;
    end
	end

endmodule