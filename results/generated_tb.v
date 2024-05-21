`timescale 1ns/1ns
module tb ();
reg [3:0]bcd;


wire [6:0]seg;
reg [6:0]seg_expected;


reg [0:10] data [0:15];

initial $readmemb("test_cases.txt", data);

integer i;
integer total_cases;
integer successful_cases;
integer failed_cases;


seg dut(
.bcd(bcd),
.seg(seg)
);

initial begin



    // setting the counters
    total_cases=0;
    successful_cases=0;
    failed_cases=0;
for (i=0; i < 16; i=i+1) begin
total_cases= total_cases+1;
{bcd,seg_expected}=data[i];
#5
if (seg== seg_expected )begin
$display("test case %d==> Success",total_cases);
$display("#####################################################");
successful_cases=successful_cases+1;
end 
 else begin
$display("test case %d==> Fail",total_cases);
$display("INPUTS:\n");
$display("bcd %b\n",bcd);
$display("OUTPUTS:\n");
$display("seg %b ==> seg_expected %b \n",seg,seg_expected);
$display("#####################################################");
failed_cases=failed_cases+1;

end
end
$display("Summary:\n total cases==>%d \n successful cases==>%d \n failed cases==>%d",total_cases,successful_cases,failed_cases);
 end
endmodule