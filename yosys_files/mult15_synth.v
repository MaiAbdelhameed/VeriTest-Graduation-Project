/* Generated by Yosys 0.41+83 (git sha1 7045cf509, x86_64-w64-mingw32-g++ 13.2.1 -Os) */

/* cells_not_processed =  1  */
/* src = "mult15.v:1.1-21.10" */
module mult15(a, b, result);
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
  wire _054_;
  wire _055_;
  wire _056_;
  wire _057_;
  wire _058_;
  wire _059_;
  wire _060_;
  wire _061_;
  wire _062_;
  wire _063_;
  wire _064_;
  wire _065_;
  wire _066_;
  wire _067_;
  wire _068_;
  wire _069_;
  wire _070_;
  wire _071_;
  wire _072_;
  wire _073_;
  wire _074_;
  wire _075_;
  wire _076_;
  wire _077_;
  wire _078_;
  wire _079_;
  wire _080_;
  wire _081_;
  wire _082_;
  wire _083_;
  wire _084_;
  wire _085_;
  wire _086_;
  wire _087_;
  wire _088_;
  wire _089_;
  wire _090_;
  wire _091_;
  wire _092_;
  wire _093_;
  wire _094_;
  wire _095_;
  wire _096_;
  wire _097_;
  wire _098_;
  wire _099_;
  wire _100_;
  wire _101_;
  wire _102_;
  wire _103_;
  wire _104_;
  wire _105_;
  wire _106_;
  wire _107_;
  wire _108_;
  wire _109_;
  wire _110_;
  wire _111_;
  wire _112_;
  wire _113_;
  wire _114_;
  wire _115_;
  wire _116_;
  wire _117_;
  wire _118_;
  wire _119_;
  wire _120_;
  wire _121_;
  wire _122_;
  wire _123_;
  wire _124_;
  wire _125_;
  wire _126_;
  wire _127_;
  wire _128_;
  wire _129_;
  wire _130_;
  wire _131_;
  wire _132_;
  wire _133_;
  wire _134_;
  wire _135_;
  wire _136_;
  wire _137_;
  wire _138_;
  wire _139_;
  wire _140_;
  wire _141_;
  wire _142_;
  wire _143_;
  wire _144_;
  wire _145_;
  wire _146_;
  wire _147_;
  wire _148_;
  wire _149_;
  wire _150_;
  /* src = "mult15.v:2.17-2.18" */
  input [3:0] a;
  wire [3:0] a;
  /* src = "mult15.v:3.17-3.18" */
  input [3:0] b;
  wire [3:0] b;
  /* src = "mult15.v:4.22-4.28" */
  output [7:0] result;
  wire [7:0] result;
  NOT _151_ (
    .A(b[3]),
    .Y(_066_)
  );
  NOT _152_ (
    .A(b[2]),
    .Y(_071_)
  );
  NOT _153_ (
    .A(b[1]),
    .Y(_072_)
  );
  NOT _154_ (
    .A(a[1]),
    .Y(_073_)
  );
  NOT _155_ (
    .A(a[2]),
    .Y(_074_)
  );
  NOT _156_ (
    .A(a[3]),
    .Y(_075_)
  );
  AND _157_ (
    .A(b[3]),
    .B(a[0]),
    .Y(_076_)
  );
  AND _158_ (
    .A(a[0]),
    .B(b[0]),
    .Y(result[0])
  );
  AND _159_ (
    .A(b[1]),
    .B(a[1]),
    .Y(_077_)
  );
  AND _160_ (
    .A(b[0]),
    .B(a[1]),
    .Y(_078_)
  );
  AND _161_ (
    .A(b[1]),
    .B(a[0]),
    .Y(_079_)
  );
  AND _162_ (
    .A(_078_),
    .B(_079_),
    .Y(_080_)
  );
  NOT _163_ (
    .A(_080_),
    .Y(_081_)
  );
  AND _164_ (
    .A(b[0]),
    .B(a[2]),
    .Y(_082_)
  );
  AND _165_ (
    .A(a[1]),
    .B(_082_),
    .Y(_083_)
  );
  AND _166_ (
    .A(_079_),
    .B(_083_),
    .Y(_084_)
  );
  OR _167_ (
    .A(_077_),
    .B(_082_),
    .Y(_085_)
  );
  AND _168_ (
    .A(a[0]),
    .B(_078_),
    .Y(_086_)
  );
  OR _169_ (
    .A(_083_),
    .B(_086_),
    .Y(_087_)
  );
  NOT _170_ (
    .A(_087_),
    .Y(_088_)
  );
  OR _171_ (
    .A(_072_),
    .B(_088_),
    .Y(_089_)
  );
  AND _172_ (
    .A(_085_),
    .B(_089_),
    .Y(_090_)
  );
  OR _173_ (
    .A(_084_),
    .B(_090_),
    .Y(_091_)
  );
  AND _174_ (
    .A(a[0]),
    .B(_091_),
    .Y(_092_)
  );
  NOT _175_ (
    .A(_092_),
    .Y(_093_)
  );
  AND _176_ (
    .A(b[0]),
    .B(a[3]),
    .Y(_094_)
  );
  OR _177_ (
    .A(b[1]),
    .B(_094_),
    .Y(_095_)
  );
  NOT _178_ (
    .A(_095_),
    .Y(_096_)
  );
  AND _179_ (
    .A(a[2]),
    .B(_094_),
    .Y(_097_)
  );
  NOT _180_ (
    .A(_097_),
    .Y(_098_)
  );
  OR _181_ (
    .A(a[2]),
    .B(_094_),
    .Y(_099_)
  );
  NOT _182_ (
    .A(_099_),
    .Y(_100_)
  );
  OR _183_ (
    .A(_097_),
    .B(_100_),
    .Y(_101_)
  );
  AND _184_ (
    .A(_098_),
    .B(_099_),
    .Y(_102_)
  );
  AND _185_ (
    .A(_088_),
    .B(_101_),
    .Y(_103_)
  );
  OR _186_ (
    .A(_087_),
    .B(_102_),
    .Y(_104_)
  );
  AND _187_ (
    .A(_087_),
    .B(_102_),
    .Y(_105_)
  );
  OR _188_ (
    .A(_088_),
    .B(_101_),
    .Y(_106_)
  );
  AND _189_ (
    .A(_104_),
    .B(_106_),
    .Y(_107_)
  );
  OR _190_ (
    .A(_103_),
    .B(_105_),
    .Y(_108_)
  );
  AND _191_ (
    .A(b[1]),
    .B(_108_),
    .Y(_109_)
  );
  OR _192_ (
    .A(_072_),
    .B(_107_),
    .Y(_110_)
  );
  AND _193_ (
    .A(_095_),
    .B(_110_),
    .Y(_111_)
  );
  OR _194_ (
    .A(_096_),
    .B(_109_),
    .Y(_112_)
  );
  AND _195_ (
    .A(a[1]),
    .B(_111_),
    .Y(_113_)
  );
  OR _196_ (
    .A(_073_),
    .B(_112_),
    .Y(_114_)
  );
  AND _197_ (
    .A(_073_),
    .B(_112_),
    .Y(_115_)
  );
  OR _198_ (
    .A(a[1]),
    .B(_111_),
    .Y(_116_)
  );
  AND _199_ (
    .A(_114_),
    .B(_116_),
    .Y(_117_)
  );
  OR _200_ (
    .A(_113_),
    .B(_115_),
    .Y(_118_)
  );
  OR _201_ (
    .A(_092_),
    .B(_117_),
    .Y(_119_)
  );
  AND _202_ (
    .A(_092_),
    .B(_117_),
    .Y(_120_)
  );
  OR _203_ (
    .A(_093_),
    .B(_118_),
    .Y(_121_)
  );
  AND _204_ (
    .A(_119_),
    .B(_121_),
    .Y(_122_)
  );
  AND _205_ (
    .A(b[2]),
    .B(_122_),
    .Y(_123_)
  );
  AND _206_ (
    .A(_071_),
    .B(_111_),
    .Y(_124_)
  );
  OR _207_ (
    .A(_123_),
    .B(_124_),
    .Y(_125_)
  );
  AND _208_ (
    .A(_076_),
    .B(_125_),
    .Y(_126_)
  );
  NOT _209_ (
    .A(_126_),
    .Y(_127_)
  );
  OR _210_ (
    .A(_076_),
    .B(_125_),
    .Y(_128_)
  );
  AND _211_ (
    .A(_127_),
    .B(_128_),
    .Y(result[3])
  );
  AND _212_ (
    .A(a[0]),
    .B(_125_),
    .Y(_129_)
  );
  NOT _213_ (
    .A(_129_),
    .Y(_130_)
  );
  AND _214_ (
    .A(_114_),
    .B(_121_),
    .Y(_131_)
  );
  OR _215_ (
    .A(_113_),
    .B(_120_),
    .Y(_132_)
  );
  OR _216_ (
    .A(a[2]),
    .B(_086_),
    .Y(_133_)
  );
  AND _217_ (
    .A(_094_),
    .B(_133_),
    .Y(_134_)
  );
  NOT _218_ (
    .A(_134_),
    .Y(_135_)
  );
  OR _219_ (
    .A(a[3]),
    .B(_083_),
    .Y(_136_)
  );
  AND _220_ (
    .A(b[1]),
    .B(_136_),
    .Y(_137_)
  );
  AND _221_ (
    .A(_075_),
    .B(_083_),
    .Y(_138_)
  );
  OR _222_ (
    .A(_134_),
    .B(_138_),
    .Y(_139_)
  );
  AND _223_ (
    .A(_135_),
    .B(_137_),
    .Y(_140_)
  );
  NOT _224_ (
    .A(_140_),
    .Y(_141_)
  );
  AND _225_ (
    .A(a[2]),
    .B(_140_),
    .Y(_142_)
  );
  OR _226_ (
    .A(_074_),
    .B(_141_),
    .Y(_143_)
  );
  OR _227_ (
    .A(a[2]),
    .B(_140_),
    .Y(_144_)
  );
  NOT _228_ (
    .A(_144_),
    .Y(_145_)
  );
  AND _229_ (
    .A(_143_),
    .B(_144_),
    .Y(_146_)
  );
  OR _230_ (
    .A(_142_),
    .B(_145_),
    .Y(_147_)
  );
  AND _231_ (
    .A(_131_),
    .B(_147_),
    .Y(_148_)
  );
  OR _232_ (
    .A(_132_),
    .B(_146_),
    .Y(_149_)
  );
  AND _233_ (
    .A(_132_),
    .B(_146_),
    .Y(_150_)
  );
  OR _234_ (
    .A(_131_),
    .B(_147_),
    .Y(_000_)
  );
  AND _235_ (
    .A(_149_),
    .B(_000_),
    .Y(_001_)
  );
  OR _236_ (
    .A(_148_),
    .B(_150_),
    .Y(_002_)
  );
  AND _237_ (
    .A(b[2]),
    .B(_002_),
    .Y(_003_)
  );
  OR _238_ (
    .A(_071_),
    .B(_001_),
    .Y(_004_)
  );
  OR _239_ (
    .A(b[2]),
    .B(_140_),
    .Y(_005_)
  );
  NOT _240_ (
    .A(_005_),
    .Y(_006_)
  );
  AND _241_ (
    .A(_004_),
    .B(_005_),
    .Y(_007_)
  );
  OR _242_ (
    .A(_003_),
    .B(_006_),
    .Y(_008_)
  );
  AND _243_ (
    .A(a[1]),
    .B(_007_),
    .Y(_009_)
  );
  OR _244_ (
    .A(_073_),
    .B(_008_),
    .Y(_010_)
  );
  AND _245_ (
    .A(_073_),
    .B(_008_),
    .Y(_011_)
  );
  OR _246_ (
    .A(a[1]),
    .B(_007_),
    .Y(_012_)
  );
  AND _247_ (
    .A(_010_),
    .B(_012_),
    .Y(_013_)
  );
  OR _248_ (
    .A(_009_),
    .B(_011_),
    .Y(_014_)
  );
  OR _249_ (
    .A(_129_),
    .B(_013_),
    .Y(_015_)
  );
  AND _250_ (
    .A(_129_),
    .B(_013_),
    .Y(_016_)
  );
  OR _251_ (
    .A(_130_),
    .B(_014_),
    .Y(_017_)
  );
  AND _252_ (
    .A(_015_),
    .B(_017_),
    .Y(_018_)
  );
  AND _253_ (
    .A(b[3]),
    .B(_018_),
    .Y(_019_)
  );
  AND _254_ (
    .A(_066_),
    .B(_007_),
    .Y(_020_)
  );
  OR _255_ (
    .A(_019_),
    .B(_020_),
    .Y(result[4])
  );
  AND _256_ (
    .A(b[1]),
    .B(_139_),
    .Y(_021_)
  );
  NOT _257_ (
    .A(_021_),
    .Y(_022_)
  );
  AND _258_ (
    .A(a[3]),
    .B(_022_),
    .Y(_023_)
  );
  NOT _259_ (
    .A(_023_),
    .Y(_024_)
  );
  AND _260_ (
    .A(_143_),
    .B(_000_),
    .Y(_025_)
  );
  OR _261_ (
    .A(_142_),
    .B(_150_),
    .Y(_026_)
  );
  AND _262_ (
    .A(_023_),
    .B(_026_),
    .Y(_027_)
  );
  OR _263_ (
    .A(_024_),
    .B(_025_),
    .Y(_028_)
  );
  OR _264_ (
    .A(_023_),
    .B(_026_),
    .Y(_029_)
  );
  AND _265_ (
    .A(_028_),
    .B(_029_),
    .Y(_030_)
  );
  OR _266_ (
    .A(_071_),
    .B(_030_),
    .Y(_031_)
  );
  AND _267_ (
    .A(a[3]),
    .B(_021_),
    .Y(_032_)
  );
  OR _268_ (
    .A(b[2]),
    .B(_032_),
    .Y(_033_)
  );
  AND _269_ (
    .A(_031_),
    .B(_033_),
    .Y(_034_)
  );
  NOT _270_ (
    .A(_034_),
    .Y(_035_)
  );
  AND _271_ (
    .A(_066_),
    .B(_034_),
    .Y(_036_)
  );
  AND _272_ (
    .A(_010_),
    .B(_017_),
    .Y(_037_)
  );
  OR _273_ (
    .A(_009_),
    .B(_016_),
    .Y(_038_)
  );
  AND _274_ (
    .A(a[2]),
    .B(_034_),
    .Y(_039_)
  );
  OR _275_ (
    .A(_074_),
    .B(_035_),
    .Y(_040_)
  );
  AND _276_ (
    .A(_074_),
    .B(_035_),
    .Y(_041_)
  );
  OR _277_ (
    .A(a[2]),
    .B(_034_),
    .Y(_042_)
  );
  AND _278_ (
    .A(_040_),
    .B(_042_),
    .Y(_043_)
  );
  OR _279_ (
    .A(_039_),
    .B(_041_),
    .Y(_044_)
  );
  AND _280_ (
    .A(_037_),
    .B(_043_),
    .Y(_045_)
  );
  AND _281_ (
    .A(_038_),
    .B(_044_),
    .Y(_046_)
  );
  OR _282_ (
    .A(_045_),
    .B(_046_),
    .Y(_047_)
  );
  AND _283_ (
    .A(b[3]),
    .B(_047_),
    .Y(_048_)
  );
  OR _284_ (
    .A(_036_),
    .B(_048_),
    .Y(result[5])
  );
  OR _285_ (
    .A(_027_),
    .B(_032_),
    .Y(_049_)
  );
  AND _286_ (
    .A(b[2]),
    .B(_049_),
    .Y(_050_)
  );
  NOT _287_ (
    .A(_050_),
    .Y(_051_)
  );
  AND _288_ (
    .A(a[3]),
    .B(_051_),
    .Y(_052_)
  );
  NOT _289_ (
    .A(_052_),
    .Y(_053_)
  );
  AND _290_ (
    .A(_038_),
    .B(_042_),
    .Y(_054_)
  );
  OR _291_ (
    .A(_037_),
    .B(_041_),
    .Y(_055_)
  );
  AND _292_ (
    .A(_040_),
    .B(_055_),
    .Y(_056_)
  );
  OR _293_ (
    .A(_039_),
    .B(_054_),
    .Y(_057_)
  );
  AND _294_ (
    .A(_052_),
    .B(_057_),
    .Y(_058_)
  );
  OR _295_ (
    .A(_053_),
    .B(_056_),
    .Y(_059_)
  );
  OR _296_ (
    .A(_052_),
    .B(_057_),
    .Y(_060_)
  );
  AND _297_ (
    .A(_059_),
    .B(_060_),
    .Y(_061_)
  );
  AND _298_ (
    .A(b[3]),
    .B(_061_),
    .Y(_062_)
  );
  AND _299_ (
    .A(_066_),
    .B(_050_),
    .Y(_063_)
  );
  OR _300_ (
    .A(_062_),
    .B(_063_),
    .Y(result[6])
  );
  OR _301_ (
    .A(_050_),
    .B(_058_),
    .Y(_064_)
  );
  AND _302_ (
    .A(b[3]),
    .B(_064_),
    .Y(result[7])
  );
  AND _303_ (
    .A(b[2]),
    .B(a[0]),
    .Y(_065_)
  );
  OR _304_ (
    .A(_091_),
    .B(_065_),
    .Y(_067_)
  );
  AND _305_ (
    .A(_091_),
    .B(_065_),
    .Y(_068_)
  );
  NOT _306_ (
    .A(_068_),
    .Y(_069_)
  );
  AND _307_ (
    .A(_067_),
    .B(_069_),
    .Y(result[2])
  );
  OR _308_ (
    .A(_078_),
    .B(_079_),
    .Y(_070_)
  );
  AND _309_ (
    .A(_081_),
    .B(_070_),
    .Y(result[1])
  );
endmodule
