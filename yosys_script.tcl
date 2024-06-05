read_verilog test_sample.v

proc; opt; fsm; opt; memory; opt

techmap; opt

flatten

abc -liberty C:\Users\Mai\OneDrive\Documents\GitHub\Verilog-Testbench-Generator-GP\gate.lib

clean -purge

write_verilog -attr2comment C:\Users\Mai\OneDrive\Documents\GitHub\Verilog-Testbench-Generator-GP\./test_sample_synth.v