"use client";
import React, { useState } from "react";
import axios from "axios";
import Image from "next/image";
import Toggle_coverage_table_component from "./Toggle_coverage_table_component";

const UploadForm = () => {
  const [vFile, setVFile] = useState(null);
  const [pyFile, setPyFile] = useState(null);
  const [errorMessage, setErrorMessage] = useState("");
  const [downloadedFile, setDownloadedFile] = useState("");
  const [ready, setReady] = useState(false);
  const [loading, setLoading] = useState(false);

  const handleVFileChange = (e) => {
    setVFile(e.target.files[0]);
  };

  const handlePyFileChange = (e) => {
    setPyFile(e.target.files[0]);
  };

  const handleSubmit = async (e) => {
    setReady(false);
    e.preventDefault();
    setLoading(true);

    // Check if files are empty
    if (!vFile || !pyFile) {
      setErrorMessage("Please select both .v and .py files.");
      return;
    }
    // check if files are in the wrong format
    else if (!(vFile.name.endsWith(".v") && pyFile.name.endsWith(".py"))) {
      setErrorMessage("Please select the files with the correct extensions.");
      return;
    } else if (
      !(
        vFile.name.split(".").slice(0, -1).join(".") ===
        pyFile.name.split(".").slice(0, -1).join(".")
      )
    ) {
      setErrorMessage("The verilog and python files must have the same name.");
      return;
    }
    // You can proceed with file upload logic here
    const formData = new FormData();
    formData.append("vFile", vFile);
    formData.append("pyFile", pyFile);
    formData.append("Mode_Number", "1");

    try {
      const response = await axios.post(
        "http://localhost:5000/upload_files",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
          responseType: "blob", // Set response type to blob
        }
      );
      setLoading(false);
      setDownloadedFile(response.data);
      setReady(true);
    } catch (error) {
      console.error("Error uploading files:", error);
    }
  };

  return (
    <div className="container mt-5">
      {errorMessage && (
        <div className="alert alert-danger" role="alert">
          {errorMessage}
        </div>
      )}
      <div className="row justify-content-center">
        <div className="col-md-10">
          <form onSubmit={handleSubmit}>
            <div className="mb-3">
              <label htmlFor="vFile" className="form-label">
                Upload .v File
              </label>
              <input
                type="file"
                className="form-control"
                id="vFile"
                accept=".v"
                onChange={handleVFileChange}
              />
            </div>
            <div className="mb-3">
              <label htmlFor="pyFile" className="form-label">
                Upload .py File
              </label>
              <input
                type="file"
                className="form-control"
                id="pyFile"
                accept=".py"
                onChange={handlePyFileChange}
              />
            </div>
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
                "Upload Files"
              )}
            </button>
          </form>

          {downloadedFile && ready && (
            <div>
              <a
                href={URL.createObjectURL(new Blob([downloadedFile]))}
                download="result.zip"
              >
                <button type="button" className="mt-2 btn btn-outline-success">
                  download the Generated testbench
                </button>
              </a>
            </div>
          )}
          {/* <Toggle_coverage_table_component /> */}
        </div>
      </div>
    </div>
  );
};

export default UploadForm;
