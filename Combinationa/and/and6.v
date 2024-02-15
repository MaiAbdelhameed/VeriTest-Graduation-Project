function logic and_function (logic a, logic b);
  begin
    and_function = a & b;
  end
endfunction

module my_module (
  // ...other ports
);

  // ...other logic
  logic result = and_function(a, b);

  // ... use result
endmodule