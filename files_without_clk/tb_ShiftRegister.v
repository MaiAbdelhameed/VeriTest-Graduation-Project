module tb_ShiftRegister  #(
    parameter DATA_BITS         = 8,
    parameter MATRIX_SIZE       = 8,
    parameter OUTPUT_SIZE       = 2*MATRIX_SIZE-1
) ();

reg clock;
reg reset;
reg load;
reg shift;
reg [DATA_BITS-1:0] data_in [0:MATRIX_SIZE-1][0:OUTPUT_SIZE-1];
wire [DATA_BITS-1:0] data_out [0:MATRIX_SIZE-1];

ShiftRegister #(
    .DATA_BITS(DATA_BITS),   
    .MATRIX_SIZE(MATRIX_SIZE),     
    .OUTPUT_SIZE(OUTPUT_SIZE)  
) DUT (
    .clock(clock),
    .reset(reset),
    .load(load),
    .shift(shift),
    .data_in(data_in),
    .data_out(data_out)
);

integer count;
initial begin
        clock = 1'b0;
        reset = 1'b0;
	load  = 1'b0;
	shift = 1'b0;
        $dumpfile("ShiftRegister.vcd") ;
        $dumpvars;
end

always begin
        #5 clock = ~clock;
        #5 clock = ~clock;
end

always @(data_out) begin
	$display("data_out[0] at %0t",data_out[0],$time);
	$display("data_out[7] at %0t",data_out[7],$time);
end

initial begin

	#10 reset = 1'b1;
        #20 reset = 1'b0;

        #200
        
	#10 load = 1'b1;
	#30 
	count=0;
        for (integer i=0;i<MATRIX_SIZE;i++)
                for (integer j =0; j< OUTPUT_SIZE;j++) begin
                        data_in[i][j]=count;
                        count= count+1;
                end

	#10 load = 1'b0;
	#100 shift = 1'b1;
        #250
	#50 shift = 1'b0;
        #50 $finish;


end

endmodule

