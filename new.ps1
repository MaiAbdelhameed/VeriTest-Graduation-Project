quartus_map ALU2 --source=ALU2.v --family="Cyclone V" 
quartus_fit ALU2
quartus_eda ALU2 --formal_verification --tool=conformal