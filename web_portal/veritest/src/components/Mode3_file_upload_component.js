"use client";
import React, { useState } from "react";
import axios from "axios";

const UploadForm = ({
  loading,
  setLoading,
  responseData,
  setResponseData,
  file,
  setFile,
}) => {
  const [vFile, setVFile] = useState(null);
  const [errorMessage, setErrorMessage] = useState("");

  const handleVFileChange = (e) => {
    setVFile(e.target.files[0]);
    setFile(e.target.files[0]);
  };

  const handleSubmit = async (e) => {
    setLoading(true);
    e.preventDefault();

    // Check if files are empty
    if (!vFile) {
      setErrorMessage("Please select a .v file");
      setLoading(false);
      return;
    }
    // Check if files are in the wrong format
    else if (!vFile.name.endsWith(".v")) {
      setErrorMessage("Please select the file with the correct extension.");
      setLoading(false);
      return;
    }

    // Proceed with file upload logic here
    const formData = new FormData();
    formData.append("vFile", vFile);
    formData.append("Mode_Number", "3");

    try {
      const response = await axios.post(
        "http://localhost:5000/upload_files",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
          responseType: "json", // Set response type to JSON
        }
      );

      setResponseData(response.data);
      setLoading(false);
    } catch (error) {
      console.error("Error uploading files:", error);
      setErrorMessage("An error occurred while uploading the file.");
      setLoading(false);
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
            <button
              type="submit"
              className="btn btn-success"
              disabled={loading}
            >
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
                "Upload File"
              )}
            </button>
          </form>

          {/* {responseData && !loading && (
            <div className="mt-3">
              <h5>Response Data:</h5>
              <pre>{JSON.stringify(responseData, null, 2)}</pre>
            </div>
          )} */}
        </div>
      </div>
    </div>
  );
};

export default UploadForm;
