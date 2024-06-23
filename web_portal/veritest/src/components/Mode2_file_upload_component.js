"use client";
import React, { useState } from "react";
import axios from "axios";
import Image from "next/image";

const UploadForm = () => {
  const [vFile, setVFile] = useState(null);
  const [jsonFile, setJsonFile] = useState(null);
  const [errorMessage, setErrorMessage] = useState("");
  const [downloadedFile, setDownloadedFile] = useState("");
  const [ready, setReady] = useState(false);
  const [loading, setLoading] = useState(false);

  const handleVFileChange = (e) => {
    setVFile(e.target.files[0]);
  };
  const handleChangeJsonFile = (e) => {
    setJsonFile(e.target.files[0]);
  };

  const handleSubmit = async (e) => {
    setReady(false);
    e.preventDefault();
    setLoading(true);
    // Check if files are empty
    if (!vFile || !jsonFile) {
      setErrorMessage("Please select both .v and .json files.");
      return;
    }
    // check if files are in the wrong format
    else if (!(vFile.name.endsWith(".v") && jsonFile.name.endsWith(".json"))) {
      setErrorMessage("Please select the files with the correct extensions.");
      return;
    } else if (
      !(
        vFile.name.split(".").slice(0, -1).join(".") ===
        jsonFile.name.split(".").slice(0, -1).join(".")
      )
    ) {
      setErrorMessage("The Verilog and JSON files must have the same name.");
      return;
    }
    // You can proceed with file upload logic here
    const formData = new FormData();
    formData.append("vFile", vFile);
    formData.append("jsonFile", jsonFile);
    formData.append("Mode_Number", "2");

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
        <div className="col-md-6">
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
                Upload .JSON File
              </label>
              <input
                type="file"
                className="form-control"
                id="jsonFile"
                accept=".json"
                onChange={handleChangeJsonFile}
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
                "Submit"
              )}
            </button>
          </form>

          {downloadedFile && ready && (
            <a
              href={URL.createObjectURL(new Blob([downloadedFile]))}
              download="result.zip"
            >
              <button type="button" className="mt-2 btn btn-outline-success">
                download the Generated testbench
              </button>
            </a>
          )}
        </div>
      </div>
    </div>
  );
};

export default UploadForm;
