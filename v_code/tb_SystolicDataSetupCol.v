module tb_SystolicDataSetupRow #(
    parameter DATA_BITS         = 8,
    parameter MATRIX_SIZE       = 8,
    parameter OUTPUT_SIZE 	= 2*MATRIX_SIZE-1
) ();

reg clock;
reg reset;

integer count;
    reg [DATA_BITS-1:0] data_in [0:MATRIX_SIZE-1][0:MATRIX_SIZE-1];
    wire [DATA_BITS-1:0] data_out [0:OUTPUT_SIZE-1][0:MATRIX_SIZE-1];

     SystolicDataSetupCol #(
                .DATA_BITS(DATA_BITS),
                .MATRIX_SIZE(MATRIX_SIZE),
                .OUTPUT_SIZE(OUTPUT_SIZE)
            ) DUT ( 

		.clock(clock),
		.reset(reset),
		.data_in(data_in),
		.data_out(data_out)
	    );


initial begin
	clock = 1'b0;
	reset = 1'b0;
	$dumpfile("Systolic.vcd") ;
     	$dumpvars;
end

always begin
	#5 clock = ~clock;
	#5 clock = ~clock;
end

initial begin

	#10 reset = 1'b1;
	#20 reset = 1'b0;

	#30
	for (integer i=0;i<MATRIX_SIZE;i++)
		for (integer j=0 ; j< MATRIX_SIZE;j++)
			data_in[i][j]=8'h00;

	#60
	count=0;
	for (integer i=0;i<MATRIX_SIZE;i++)
		for (integer j =0; j< MATRIX_SIZE;j++) begin
			data_in[i][j]=count;
			count= count+1;
		end

	#50
	count=0;
	for (integer i=0;i<MATRIX_SIZE;i++)
		for (integer j=0 ; j< MATRIX_SIZE;j++) begin
			data_in[i][j]=count+3;
			count= count+1;
		end

	#50 $finish;

end



endmodule

