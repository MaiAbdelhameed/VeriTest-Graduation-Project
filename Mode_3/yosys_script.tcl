read_verilog test_sample.v

proc; opt; fsm; opt; memory; opt

techmap; opt

flatten

abc -liberty /home/mark/Grad_Project/VeriTest_clean/Mode_3/gate.lib

clean -purge

write_verilog -attr2comment /home/mark/Grad_Project/VeriTest_clean/Mode_3/./test_sample_synth.v