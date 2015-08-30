describe("Synth test", function() {
  it("play", function() {
    var setting = {
      synthDef: {
        ugen: "flock.ugen.sin",
        freq: {
          ugen: "flock.ugen.lfNoise",
          freq: 5,
          mul: 700,
          add: 60
        },
        mul: 0.9
      }
    };
    var synth = new LAUGH.Synth("fm", setting);
  });
});
