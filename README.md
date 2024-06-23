# Verilog-Testbench-Generator-GP

## Overview
This repository contains a tool for generating testbenches for Verilog files. The tool operates in three distinct modes based on user input, providing flexibility for different stages of the verification process. The core idea is to automate the generation of test cases and expected outputs, easing the verification process of digital circuits described in Verilog.

## Modes of Operation
### Mode 1: Golden Model
Input: A Verilog file and a Python file containing a golden model.
Process:
  Generates test cases.
  Computes expected outputs using the golden model.
  Generates a Verilog testbench that tests the given Verilog file using the generated test cases and expected results.
Diagram:
 <!-- Update with correct path to the image -->

### Mode 2: Specifications
Input: A Verilog file and a JSON file containing specifications about the circuit.
Process:
Analyzes the JSON file to construct a Python file containing a golden model of the circuit.
Executes Mode 1 using the generated Python code as the golden model and the provided Verilog file.
Diagram:
 <!-- Update with correct path to the image -->

### Mode 3: Predict Functionality
Input: A Verilog file.
Process:
Generates a prediction using the GNN model embeddings trained on an SVM model.
Creates a specs JSON in the same format as Mode 2.
The user confirms the details in the JSON.
Executes the cycle as in Mode 2.

### Experiments:
Includes experiments with pure classical methods, pure GNN methods, and classical methods trained on GNN embeddings.
Diagram:
 <!-- Update with correct path to the image -->


### Installation
To set up the project, follow these steps:

1. Clone the repository:
<insert code snippet>
2. Install dependencies:
<insert code snippet>

### Usage

### Project Structure

### Future Work
#### Coverage Enhancement
1. Expanded Coverage Metrics
2. Support for Larger and More Complex Designs

#### Test Set Optimization
1. Enhanced SMT Solver Integration
2. Adaptive Random Stimuli Generation
3. Hybrid Approach for Test Case Generation
4. Incremental Coverage Feedback

#### Additional Features
1. Support for Sequential Circuits
2. Deployment of a Web Interface
3. VS Code Extension
4. Publication of Manually Created Dataset
5. Research Paper on Predicting Verilog Codes using GNNs

### Contributors
Mai Abdelhameed
Malak Mokhtar
Mohammed Mohsen
Mark Milad
