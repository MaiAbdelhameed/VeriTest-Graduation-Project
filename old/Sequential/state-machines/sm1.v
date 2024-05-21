module simple_state_machine (
  input clk,
  input reset,
  input some_input,
  output reg some_output
);

  reg [2:0] state = 3'b000; // Initial state

  always_ff @(posedge clk, posedge reset) begin
    if (reset) begin
      state <= 3'b000; // Reset state
    end else begin
      case (state)
        3'b000: begin
          if (some_input) begin
            state <= 3'b001;
          end
        end
        3'b001: begin
          some_output <= 1;
          state <= 3'b010;
        end
        3'b010: begin
          some_output <= 0;
          state <= 3'b000;
        end
        default: state <= 3'b000;
      endcase
    end
  end

endmodule
