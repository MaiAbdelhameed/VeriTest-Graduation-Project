module comparator3 (A,B,C,D,E);
    input A,B;
    output C,D,E;

    assign C = (~A) & B; // A<B
    assign E = (~B) & A; // A>B
    assign D = ~(C | E); // A=B
    
endmodule