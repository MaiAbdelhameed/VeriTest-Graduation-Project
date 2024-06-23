import React from "react";

import Navbar_component from "@/components/Navbar_component";
import Mode1_documentation_component from "@/components/Mode1_documentation_component";
import Mode1_file_upload_component from "@/components/Mode1_file_upload_component";
export default function mode1() {
  return (
    <div>
      <Navbar_component />

      <div className="d-flex  flex-column justify-content-center ">
        <Mode1_documentation_component />
        <Mode1_file_upload_component />
      </div>
    </div>
  );
}
