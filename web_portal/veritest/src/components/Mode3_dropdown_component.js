"use client";
import React from "react";

const DropdownFormControl = ({
  label,
  options,
  selectedItems,
  onSelect,
  onRemove,
}) => {
  const handleSelect = (e) => {
    const option = e.target.value;
    if (option) {
      onSelect(option);
    }
    e.target.value = ""; // Reset the dropdown selection
  };

  return (
    <div>
      <div className="input-group mb-3">
        <span className="input-group-text" id="basic-addon2">
          {label}
        </span>
        <select
          id={label}
          className="form-select"
          onChange={handleSelect}
          value=""
        >
          <option value="" disabled>
            Select an option
          </option>
          {options.map((option, index) => (
            <option key={index} value={option}>
              {option}
            </option>
          ))}
        </select>
      </div>
      <ul className="list-group mt-3">
        {selectedItems.map((item, index) => (
          <li
            key={index}
            className="list-group-item d-flex justify-content-between align-items-center bg-dark text-white"
          >
            {item}
            <button
              type="button"
              className="btn btn-outline-danger btn-sm"
              onClick={() => onRemove(item)}
            >
              &times;
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default DropdownFormControl;
