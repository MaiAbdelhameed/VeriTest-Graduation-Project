read_verilog /home/mark/Grad_Project/VeriTest_clean/web_portal/backend/uploaded_files/decoder_test.v

proc; opt; fsm; opt; memory; opt

techmap; opt

flatten

abc -liberty /home/mark/Grad_Project/VeriTest_clean/Mode_3/gate.lib

clean -purge

write_verilog -attr2comment /home/mark/Grad_Project/VeriTest_clean/web_portal/backend/uploaded_files/decoder_test_synth.v