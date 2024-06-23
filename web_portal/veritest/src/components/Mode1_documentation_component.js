import CodeBlock from "./Code_block";

export default function Mode1_documentation_component() {
  const verilog_code = `//Verilog module.
  module seg(
      bcd,
      seg
      );
      
       //Declare inputs,outputs and internal variables.
      input [3:0] bcd;
      output [6:0] seg;
      reg [6:0] seg;
  
  //always block for converting bcd digit into 7 segment format
      always @(bcd)
      begin
          if(bcd == 0)
              seg = 7'b1111110;
          else if(bcd == 1)
              seg = 7'b0110000;
          else if(bcd == 2)
              seg = 7'b1101101;
          else if(bcd == 3)
              seg = 7'b1111001;
          else if(bcd == 4)
              seg = 7'b0110011;
          else if(bcd == 5)
              seg = 7'b1011011;
          else if(bcd == 6)
              seg = 7'b1011111;
          else if(bcd == 7)
              seg = 7'b1110000;
          else if(bcd == 8)
              seg = 7'b1111111;
          else if(bcd == 9)
              seg = 7'b1111011;
          
          else if(bcd == 10)
              seg = 7'b1110111;
          
          else if(bcd == 11)
              seg = 7'b0011111;
          
          else if(bcd == 12)
              seg = 7'b1001110;
          
          else if(bcd == 13)
              seg = 7'b0111101;
          
          else if(bcd == 14)
              seg = 7'b1001111;
          else if(bcd == 15)
              seg = 7'b1000111;
          
      end
      
  endmodule`;

  const python_model_code = `def compute(inputs):
	input_string= inputs['bcd']
	output_string = "0000000"
	input_number = int(input_string, 2)
	if input_number == 0:
		output_string = "1111110"
	elif input_number == 1:
		output_string = "0110000"
	elif input_number == 2:
		output_string = "1101101"
	elif input_number == 3:
		output_string = "1111001"
	elif input_number == 4:
		output_string = "0110011"
	elif input_number == 5:
		output_string = "1011011"
	elif input_number == 6:
		output_string = "1011111"
	elif input_number == 7:
		output_string = "1110000"
	elif input_number == 8:
		output_string = "1111111"
	elif input_number == 9:
		output_string = "1111011"
	elif input_number == 10:
		output_string = "1110111"
	elif input_number == 11:
		output_string = "0011111"
	elif input_number == 12:
		output_string = "1001110"
	elif input_number == 13:
		output_string = "0111101"
	elif input_number == 14:
		output_string = "1001111"
	elif input_number == 15:
		output_string = "1000111"
	seg=output_string
	return { "seg": seg }
`;

  return (
    <div className="container">
      <div className="row">
        <div className="col pt-2">
          <div className="mb-5">
            <h1> Mode 1</h1>
          </div>
          <p>
            In Mode 1 you must provide 2 files a <strong>Verilog file</strong>
            and a <strong> Python file</strong> to be able to generate your
            testbench
          </p>
          <hr />
          <h2> Verilog File</h2>
          <p>
            for the <strong>verilog file</strong> the module in the file must be
            named the same as the name of the file
          </p>
          <p>
            <strong>for example:</strong> seg.v
          </p>
          <CodeBlock code={verilog_code} />
          <hr />
          <h2>Python Golden Model file</h2>
          <p>
            for the <strong>Python Golden Model file</strong> it must have one
            function called compute that takes one input called
            <strong>inputs</strong> and the function should return an object
            with the key being the name of the output and the value being the
            binary string representing the return value
            <strong>
              The file must be named by the same name of the Verilog file
            </strong>
          </p>
          <strong>for example:</strong> seg.py
          <CodeBlock code={python_model_code} />
        </div>

        <div className="mt-5">
          <div className="text-center">
            <h1> Upload your files to get started 😄</h1>
          </div>
        </div>
      </div>
    </div>
  );
}
