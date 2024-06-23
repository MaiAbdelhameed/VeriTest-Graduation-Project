"use client";
import React, { useEffect } from "react";

const CodeBlock = ({ code }) => {
  return (
    <div
      style={{
        backgroundColor: "#F8F9FA",
        overflowY: "auto",
        maxHeight: "300px",
        padding: "10px",
        borderRadius: "5px",
      }}
    >
      <pre className="text-start">
        <code>{code}</code>
      </pre>
    </div>
  );
};

export default CodeBlock;
