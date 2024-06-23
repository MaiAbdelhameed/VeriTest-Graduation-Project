import React from "react";

import TOGGLE_DATA from "../../public/toggle.json";

export default function Toggle_coverage_table_component() {
  return (
    <div className="mt-5">
      <hr />
      <h2>Toggle Coverage</h2>
      <table className="table table-striped table-hover table-bordered rounded-3">
        <thead>
          <tr className="table-dark">
            <th scope="col">Name</th>
            <th scope="col">Toggle</th>
            <th scope="col">{"Toggle 1->0"}</th>
            <th scope="col">{"Toggle 0->1"}</th>
          </tr>
        </thead>
        <tbody>
          {TOGGLE_DATA.map((item) => (
            <tr>
              <th scope="row">{item.Name}</th>
              <td
                className={
                  item.value[0] == "YES" ? "table-success" : "table-danger"
                }
              >
                {item.value[0]}
              </td>
              <td
                className={
                  item.value[1] == "YES" ? "table-success" : "table-danger"
                }
              >
                {item.value[1]}
              </td>
              <td
                className={
                  item.value[2] == "YES" ? "table-success" : "table-danger"
                }
              >
                {item.value[2]}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
