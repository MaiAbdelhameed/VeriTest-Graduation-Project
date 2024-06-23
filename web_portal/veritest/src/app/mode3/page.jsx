"use client";
import React, { useState } from "react";

import Navbar_component from "@/components/Navbar_component";
import Mode3_documentation_component from "@/components/Mode3_documentation_component";
import Mode3_file_upload_component from "@/components/Mode3_file_upload_component";
import Mode3_form_component from "@/components/Mode3_form_component";
export default function mode1() {
  const [loading, setLoading] = useState(false);
  const [responseData, setResponseData] = useState(null);
  const [file, setFile] = useState();

  return (
    <div>
      <Navbar_component />

      <div className="d-flex  flex-column justify-content-center ">
        <Mode3_documentation_component />
        <Mode3_file_upload_component
          loading={loading}
          setLoading={setLoading}
          responseData={responseData}
          setResponseData={setResponseData}
          file={file}
          setFile={setFile}
        />
      </div>
      <div className="container text-center">
        <div className="row-lg-6">
          {!loading && responseData && typeof file !== "undefined" && (
            <div>
              <Mode3_form_component
                responseData={responseData}
                ready={true}
                file={file}
              />
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
