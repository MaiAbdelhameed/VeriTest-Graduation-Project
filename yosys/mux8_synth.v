/* Generated by Yosys 0.41+83 (git sha1 7045cf509, x86_64-w64-mingw32-g++ 13.2.1 -Os) */

/* cells_not_processed =  1  */
/* src = "mux8.v:3.1-17.10" */
module mux8(a, b, c, d, sel, y);
  wire _000_;
  wire _001_;
  wire _002_;
  wire _003_;
  wire _004_;
  wire _005_;
  wire _006_;
  wire _007_;
  wire _008_;
  wire _009_;
  wire _010_;
  wire _011_;
  wire _012_;
  wire _013_;
  wire _014_;
  wire _015_;
  wire _016_;
  wire _017_;
  wire _018_;
  wire _019_;
  wire _020_;
  wire _021_;
  wire _022_;
  wire _023_;
  wire _024_;
  wire _025_;
  wire _026_;
  wire _027_;
  wire _028_;
  wire _029_;
  wire _030_;
  wire _031_;
  wire _032_;
  wire _033_;
  wire _034_;
  wire _035_;
  wire _036_;
  wire _037_;
  wire _038_;
  wire _039_;
  wire _040_;
  wire _041_;
  wire _042_;
  wire _043_;
  wire _044_;
  wire _045_;
  wire _046_;
  wire _047_;
  wire _048_;
  wire _049_;
  wire _050_;
  wire _051_;
  wire _052_;
  wire _053_;
  /* src = "mux8.v:3.26-3.27" */
  input [7:0] a;
  wire [7:0] a;
  /* src = "mux8.v:3.29-3.30" */
  input [7:0] b;
  wire [7:0] b;
  /* src = "mux8.v:3.32-3.33" */
  input [7:0] c;
  wire [7:0] c;
  /* src = "mux8.v:3.35-3.36" */
  input [7:0] d;
  wire [7:0] d;
  /* src = "mux8.v:4.41-4.44" */
  input [1:0] sel;
  wire [1:0] sel;
  /* src = "mux8.v:5.46-5.47" */
  output [7:0] y;
  wire [7:0] y;
  not _054_ (
    .A(sel[1]),
    .Y(_004_)
  );
  not _055_ (
    .A(sel[0]),
    .Y(_005_)
  );
  AND _056_ (
    .A(sel[1]),
    .B(_005_),
    .Y(_006_)
  );
  AND _057_ (
    .A(c[0]),
    .B(_006_),
    .Y(_007_)
  );
  AND _058_ (
    .A(_004_),
    .B(_005_),
    .Y(_008_)
  );
  AND _059_ (
    .A(a[0]),
    .B(_008_),
    .Y(_009_)
  );
  OR _060_ (
    .A(_007_),
    .B(_009_),
    .Y(_010_)
  );
  AND _061_ (
    .A(_004_),
    .B(sel[0]),
    .Y(_011_)
  );
  AND _062_ (
    .A(b[0]),
    .B(_011_),
    .Y(_012_)
  );
  AND _063_ (
    .A(sel[1]),
    .B(sel[0]),
    .Y(_013_)
  );
  AND _064_ (
    .A(d[0]),
    .B(_013_),
    .Y(_014_)
  );
  OR _065_ (
    .A(_012_),
    .B(_014_),
    .Y(_015_)
  );
  OR _066_ (
    .A(_010_),
    .B(_015_),
    .Y(y[0])
  );
  AND _067_ (
    .A(d[1]),
    .B(_013_),
    .Y(_016_)
  );
  AND _068_ (
    .A(c[1]),
    .B(_006_),
    .Y(_017_)
  );
  OR _069_ (
    .A(_016_),
    .B(_017_),
    .Y(_018_)
  );
  AND _070_ (
    .A(a[1]),
    .B(_008_),
    .Y(_019_)
  );
  AND _071_ (
    .A(b[1]),
    .B(_011_),
    .Y(_020_)
  );
  OR _072_ (
    .A(_019_),
    .B(_020_),
    .Y(_021_)
  );
  OR _073_ (
    .A(_018_),
    .B(_021_),
    .Y(y[1])
  );
  AND _074_ (
    .A(b[2]),
    .B(_011_),
    .Y(_022_)
  );
  AND _075_ (
    .A(c[2]),
    .B(_006_),
    .Y(_023_)
  );
  OR _076_ (
    .A(_022_),
    .B(_023_),
    .Y(_024_)
  );
  AND _077_ (
    .A(d[2]),
    .B(_013_),
    .Y(_025_)
  );
  AND _078_ (
    .A(a[2]),
    .B(_008_),
    .Y(_026_)
  );
  OR _079_ (
    .A(_025_),
    .B(_026_),
    .Y(_027_)
  );
  OR _080_ (
    .A(_024_),
    .B(_027_),
    .Y(y[2])
  );
  AND _081_ (
    .A(d[3]),
    .B(_013_),
    .Y(_028_)
  );
  AND _082_ (
    .A(c[3]),
    .B(_006_),
    .Y(_029_)
  );
  OR _083_ (
    .A(_028_),
    .B(_029_),
    .Y(_030_)
  );
  AND _084_ (
    .A(a[3]),
    .B(_008_),
    .Y(_031_)
  );
  AND _085_ (
    .A(b[3]),
    .B(_011_),
    .Y(_032_)
  );
  OR _086_ (
    .A(_031_),
    .B(_032_),
    .Y(_033_)
  );
  OR _087_ (
    .A(_030_),
    .B(_033_),
    .Y(y[3])
  );
  AND _088_ (
    .A(b[4]),
    .B(_011_),
    .Y(_034_)
  );
  AND _089_ (
    .A(c[4]),
    .B(_006_),
    .Y(_035_)
  );
  OR _090_ (
    .A(_034_),
    .B(_035_),
    .Y(_036_)
  );
  AND _091_ (
    .A(d[4]),
    .B(_013_),
    .Y(_037_)
  );
  AND _092_ (
    .A(a[4]),
    .B(_008_),
    .Y(_038_)
  );
  OR _093_ (
    .A(_037_),
    .B(_038_),
    .Y(_039_)
  );
  OR _094_ (
    .A(_036_),
    .B(_039_),
    .Y(y[4])
  );
  AND _095_ (
    .A(b[5]),
    .B(_011_),
    .Y(_040_)
  );
  AND _096_ (
    .A(c[5]),
    .B(_006_),
    .Y(_041_)
  );
  OR _097_ (
    .A(_040_),
    .B(_041_),
    .Y(_042_)
  );
  AND _098_ (
    .A(d[5]),
    .B(_013_),
    .Y(_043_)
  );
  AND _099_ (
    .A(a[5]),
    .B(_008_),
    .Y(_044_)
  );
  OR _100_ (
    .A(_043_),
    .B(_044_),
    .Y(_045_)
  );
  OR _101_ (
    .A(_042_),
    .B(_045_),
    .Y(y[5])
  );
  AND _102_ (
    .A(a[6]),
    .B(_008_),
    .Y(_046_)
  );
  AND _103_ (
    .A(c[6]),
    .B(_006_),
    .Y(_047_)
  );
  OR _104_ (
    .A(_046_),
    .B(_047_),
    .Y(_048_)
  );
  AND _105_ (
    .A(d[6]),
    .B(_013_),
    .Y(_049_)
  );
  AND _106_ (
    .A(b[6]),
    .B(_011_),
    .Y(_050_)
  );
  OR _107_ (
    .A(_049_),
    .B(_050_),
    .Y(_051_)
  );
  OR _108_ (
    .A(_048_),
    .B(_051_),
    .Y(y[6])
  );
  AND _109_ (
    .A(d[7]),
    .B(_013_),
    .Y(_052_)
  );
  AND _110_ (
    .A(c[7]),
    .B(_006_),
    .Y(_053_)
  );
  OR _111_ (
    .A(_052_),
    .B(_053_),
    .Y(_000_)
  );
  AND _112_ (
    .A(a[7]),
    .B(_008_),
    .Y(_001_)
  );
  AND _113_ (
    .A(b[7]),
    .B(_011_),
    .Y(_002_)
  );
  OR _114_ (
    .A(_001_),
    .B(_002_),
    .Y(_003_)
  );
  OR _115_ (
    .A(_000_),
    .B(_003_),
    .Y(y[7])
  );
endmodule