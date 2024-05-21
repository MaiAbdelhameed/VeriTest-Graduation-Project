module one_hot_state_machine (
  input clk,
  input reset,
  input some_input,
  output reg some_output
);

  reg [2:0] state = 3'b001; // Initial state (state 0)

  always_ff @(posedge clk, posedge reset) begin
    if (reset) begin
      state <= 3'b001; // Reset state
    end else begin
      case (state)
        3'b001: begin
          if (some_input) begin
            state <= 3'b010;
          end
        end
        3'b010: begin
          some_output <= 1;
          state <= 3'b100;
        end
        3'b100: begin
          some_output <= 0;
          state <= 3'b001;
        end
        default: state <= 3'b001;
      endcase
    end
  end

endmodule
