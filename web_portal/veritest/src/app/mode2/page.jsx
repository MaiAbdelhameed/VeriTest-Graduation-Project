import React from "react";

import Navbar_component from "@/components/Navbar_component";
import Mode2_documentation_component from "@/components/Mode2_documentation_component";
import Mode2_file_upload_component from "@/components/Mode2_file_upload_component";
export default function mode1() {
  return (
    <div>
      <Navbar_component />

      <div className="d-flex  flex-column justify-content-center ">
        <Mode2_documentation_component />
        <Mode2_file_upload_component />
      </div>
    </div>
  );
}
