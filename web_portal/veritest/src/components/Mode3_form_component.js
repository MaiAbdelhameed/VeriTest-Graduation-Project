"use client";
import { useState, useEffect } from "react";
import DropdownFormControl from "@/components/Mode3_dropdown_component";
import axios from "axios";

const MyForm = ({ responseData, ready, file }) => {
  // helper functions
  function parseStringToObject(str) {
    const obj = {};
    const pairs = str.split(" ");

    pairs.forEach((pair) => {
      const [key, value] = pair.split(":");
      obj[key] = isNaN(value) ? value : Number(value);
    });

    return obj;
  }
  // constants
  // circuit Types
  const circuitTypes = [
    "adder",
    "decoder",
    "encoder",
    "mux",
    "not",
    "seg",
    "and",
    "nand",
    "or",
    "nor",
    "xor",
    "xnor",
  ];

  // States
  const [inputOptions, setInputOptions] = useState([]);
  const [selectedInputs, setSelectedInputs] = useState([]);

  const [outputOptions, setOutputOptions] = useState([]);
  const [selectedOutputs, setSelectedOutputs] = useState([]);

  const [circuitType, setCircuitType] = useState("");

  const [modelName, setModelName] = useState("");

  const [downloadUrl, setDownloadUrl] = useState(null);
  const [loading, setLoading] = useState(false);
  /////////////////////////////////////////
  // gate circuit type
  const [gateTypeOperationType, setGateTypeOperationType] = useState("");
  /////////////////////////////////////////
  // decoder, encoder and seven_segment
  const [encoderTypeInputMode, setEncoderTypeInputMode] = useState("");
  const [encoderTypeOutputMode, setEncoderTypeOutputMode] = useState("");
  /////////////////////////////////////////

  // state handlers
  const handleSelectInput = (option) => {
    setInputOptions(inputOptions.filter((opt) => opt !== option));
    setSelectedInputs([...selectedInputs, option]);
  };

  const handleRemoveInput = (option) => {
    setSelectedInputs(selectedInputs.filter((item) => item !== option));
    setInputOptions([...inputOptions, option]);
  };

  const handleSelectOutput = (option) => {
    setOutputOptions(outputOptions.filter((opt) => opt !== option));
    setSelectedOutputs([...selectedOutputs, option]);
  };

  const handleRemoveOutput = (option) => {
    setSelectedOutputs(selectedOutputs.filter((item) => item !== option));
    setOutputOptions([...outputOptions, option]);
  };

  const handleCircuitTypeChange = (e) => {
    setCircuitType(e.target.value);
  };
  const handleModelNameChange = (e) => {
    setModelName(e.target.value);
  };

  const handleEncoderTypeInputModeChange = (e) => {
    setEncoderTypeInputMode(e.target.value);
  };
  const handleEncoderTypeOutputModeChange = (e) => {
    setEncoderTypeOutputMode(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    setLoading(true);
    const formData = new FormData();
    if (["and", "nand", "or", "nor", "xor", "xnor"].includes(circuitType)) {
      var requestData = {
        model_name: `${modelName}`,
        type: `${circuitType}`,
        operation_type: `${gateTypeOperationType}`,
        inputs: [],
        output: "",
      };

      selectedInputs.map((input, index) => {
        let result = parseStringToObject(input);
        requestData.inputs.push(result);
      });
      requestData.output = selectedOutputs[0];

      // console.log(file);

      formData.append("json", JSON.stringify(requestData));
      formData.append("vFile", file);
    } else if (["decoder", "encoder", "seg"].includes(circuitType)) {
      var requestData = {
        model_name: `${modelName}`,
        type: `${circuitType}`,
        input_mode: `${encoderTypeInputMode}`,
        output_mode: `${encoderTypeOutputMode}`,
        inputs: [],
        output: [],
      };
      selectedInputs.map((input, index) => {
        let result = parseStringToObject(input);
        requestData.inputs.push(result);
      });
      selectedOutputs.map((output, index) => {
        let result = parseStringToObject(output);
        requestData.output.push(result);
      });
      formData.append("json", JSON.stringify(requestData));
      formData.append("vFile", file);
    }

    axios
      .post("http://localhost:5000/submit_prediction", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
        responseType: "blob",
      })
      .then((response) => {
        // console.log(response.data);
        const blobUrl = window.URL.createObjectURL(new Blob([response.data]));
        setDownloadUrl(blobUrl);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  };
  const handleDownload = () => {
    const link = document.createElement("a");
    link.href = downloadUrl;
    link.setAttribute("download", "results.zip");
    document.body.appendChild(link);
    link.click();
    // Cleanup
    URL.revokeObjectURL(downloadUrl);
  };
  /////////////////////////////////////////
  // gate circuit type
  const handleGateTypeOperationTypeChange = (e) => {
    setGateTypeOperationType(e.target.value);
  };
  /////////////////////////////////////////
  // code runs once in the start to fill out form fields
  useEffect(() => {
    // Code to run once when the component mounts
    // console.log(file);
    let data = responseData;

    // checking on the type

    setModelName(data["model_name"]);
    setCircuitType(data.type);

    data.inputs.map((input, index) => {
      const newItem = `name:${input.name} size:${input.size}`;

      // Check if the newItem already exists in selectedInputs
      setSelectedInputs((prevSet) => {
        const newSet = new Set(prevSet);
        newSet.add(newItem);
        return [...newSet];
      });
    });

    if (["and", "nand", "or", "nor", "xor", "xnor"].includes(data.type)) {
      setSelectedOutputs((prevSet) => {
        const newSet = new Set(prevSet);
        newSet.add(data.output);
        return [...newSet];
      });
      setGateTypeOperationType(data["operation_type"]);
    } else if (["decoder", "encoder", "seg"].includes(data.type)) {
      data.output.map((output, index) => {
        const newItem = `name:${output.name} size:${output.size}`;

        // Check if the newItem already exists in selectedOutputs
        setSelectedOutputs((prevSet) => {
          const newSet = new Set(prevSet);
          newSet.add(newItem);
          return [...newSet];
        });
      });
      setEncoderTypeInputMode(data["input_mode"]);
      setEncoderTypeOutputMode(data["output_mode"]);
    }
  }, [ready]);

  /////////////////////////////////////////

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <h1 className="text-center mt-4">Specifications</h1>
        <div className="row">
          <div className="col">
            <div className="input-group input-group-md mb-3">
              <span className="input-group-text" id="inputGroup-sizing-sm">
                Model Name
              </span>
              <input
                type="text"
                className="form-control"
                value={modelName}
                onChange={handleModelNameChange}
              />
            </div>
          </div>
          <div className="col">
            <div className="input-group mb-3">
              <label className="input-group-text" htmlFor="circuit_type">
                Type
              </label>
              <select
                className="form-select"
                id="circuit_type"
                value={circuitType}
                onChange={handleCircuitTypeChange}
              >
                <option value="" disabled>
                  Choose...
                </option>
                {circuitTypes.map((option, index) => (
                  <option key={index} value={option}>
                    {option}
                  </option>
                ))}
              </select>
            </div>
          </div>
        </div>
        <div className="row">
          <div className="col">
            <DropdownFormControl
              label="Inputs"
              options={inputOptions}
              selectedItems={selectedInputs}
              onSelect={handleSelectInput}
              onRemove={handleRemoveInput}
            />
          </div>
          <div className="col">
            <DropdownFormControl
              label="Outputs"
              options={outputOptions}
              selectedItems={selectedOutputs}
              onSelect={handleSelectOutput}
              onRemove={handleRemoveOutput}
            />
          </div>
        </div>
        {/* gate specification fields */}
        {["and", "nand", "or", "nor", "xor", "xnor"].includes(circuitType) && (
          <div>
            <hr />
            <div className="input-group mb-3">
              <label className="input-group-text" htmlFor="gate_operation_type">
                Operation Type
              </label>
              <select
                className="form-select"
                id="gate_operation_type"
                value={gateTypeOperationType}
                onChange={handleGateTypeOperationTypeChange}
              >
                <option value="" disabled>
                  Choose...
                </option>
                <option value="logical">logical</option>
                <option value="bitwise">bitwise</option>
              </select>
            </div>
          </div>
        )}
        {/* decoder,encoder,seven_segment specification field */}
        {["decoder", "encoder", "seg"].includes(circuitType) && (
          <div>
            <hr />
            <div className="input-group input-group-md mb-3">
              <span className="input-group-text" id="inputGroup-sizing-sm">
                Input Mode
              </span>
              <select
                className="form-select"
                id="gate_operation_type"
                value={encoderTypeInputMode}
                onChange={handleEncoderTypeInputModeChange}
              >
                <option value="" disabled>
                  Choose...
                </option>
                <option value="separate">separate</option>
                <option value="concatenated">concatenated</option>
              </select>
            </div>

            <div className="input-group input-group-md mb-3">
              <span className="input-group-text" id="inputGroup-sizing-sm">
                Output Mode
              </span>
              <select
                className="form-select"
                id="gate_operation_type"
                value={encoderTypeOutputMode}
                onChange={handleEncoderTypeOutputModeChange}
              >
                <option value="" disabled>
                  Choose...
                </option>
                <option value="separate">separate</option>
                <option value="concatenated">concatenated</option>
              </select>
            </div>
          </div>
        )}
        <div className="mt-3">
          <button type="submit" className="btn btn-success">
            {loading ? (
              <div>
                <span
                  className="spinner-border spinner-border-sm"
                  aria-hidden="true"
                ></span>
                <span class="ms-2" role="status">
                  Uploading...
                </span>
              </div>
            ) : (
              "Submit"
            )}
          </button>
        </div>
      </form>
      {downloadUrl && (
        <button
          type="button"
          className="btn btn-outline-success btn-lg mt-3"
          onClick={handleDownload}
        >
          Download Zip File
        </button>
      )}
    </div>
  );
};

export default MyForm;
