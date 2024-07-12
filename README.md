# Verilog-Testbench-Generator-GP

## Overview
This repository contains a tool for generating testbenches for Verilog files. The tool operates in three distinct modes based on user input, providing flexibility for different stages of the verification process. The core idea is to automate the generation of test cases and expected outputs, easing the verification process of digital circuits described in Verilog.

## Modes of Operation
### Mode 1: Golden Model
* Diagram <br>
 ![Mode 1](https://github.com/MaiAbdelhameed/Verilog-Testbench-Generator-GP/assets/82734074/e8db7c95-050f-44bd-b7b0-80249eddda06)

* Input <br>
A Verilog file and a Python file containing a golden model.<br>

* Process <br>
  * Generates test cases.<br>
  * Computes expected outputs using the golden model.<br>
  * Generates a Verilog testbench that tests the given Verilog file using the generated test cases and expected results.<br>


### Mode 2: Specifications<br>
* Diagram<br>
 ![Mode 2](https://github.com/MaiAbdelhameed/Verilog-Testbench-Generator-GP/assets/82734074/82b867b9-1b1e-4540-a4f3-8678ffb0089f)

* Input <br> 
A Verilog file and a JSON file containing specifications about the circuit.<br>
* Process:
  * Analyzes the JSON file to construct a Python file containing a golden model of the circuit.
  *  Executes Mode 1 using the generated Python code as the golden model and the provided Verilog file.


### Mode 3: Predict Functionality
* Diagram <br>
![Mode 3](https://github.com/MaiAbdelhameed/Verilog-Testbench-Generator-GP/assets/82734074/d795f4ce-08d6-4888-b43e-a8a2de91134a)

* Input <br>
A Verilog file. <br>

* Process<br>
  * Generates a prediction using the GNN model embeddings trained on an SVM model. <br>
  * Creates a specs JSON in the same format as Mode 2. <br>
  * The user confirms the details in the JSON. <br> 
  * Executes the cycle as in Mode 2. <br> 

## Experiments:
Includes experiments with pure classical methods, pure GNN methods, and classical methods trained on GNN embeddings.

## Installation
To set up the project, follow these steps:

1. Clone the repository:
```
git clone [https://github.com/your-repo-name.git](https://github.com/MaiAbdelhameed/VeriTest-Graduation-Project.git)
cd VeriTest-Graduation-Project
```

2. Install dependencies:
```
pip install -r requirements.txt
```

## Usage
(website tutorial)

## Future Work
### Coverage Enhancement
1. Expanded Coverage Metrics
2. Support for Larger and More Complex Designs

### Test Set Optimization
1. Enhanced SMT Solver Integration
2. Adaptive Random Stimuli Generation
3. Hybrid Approach for Test Case Generation
4. Incremental Coverage Feedback

### Additional Features
1. Support for Sequential Circuits
2. Sponsorship Opportunities
3. VS Code Extension
4. Publication of Manually Created Dataset
5. Publication of Research Paper on Predicting Verilog Codes using GNNs

## Contributors & their parts
[Mai Abdelhameed](https://github.com/MaiAbdelhameed) : AI tools, research and experiments <br>
[Malak Mokhtar](https://github.com/Malak-Mokhtar) : Coverage Parser & Test Set Optimization<br>
[Mohammed Mohsen](https://github.com/Makoish) : Verilog Parser and Toggle Coverage <br>
[Mark Milad](https://github.com/helloworld877) : Golden Model and Output Generation, and Website Integration <br>



For more info about our project, you can check our presentation slides here: https://docs.google.com/presentation/d/1y-4pfcGbEakUpIj5VloSzB5nLqj5NzFL1iZe69CHcl4/edit#slide=id.p
