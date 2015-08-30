describe("Score test", function() {
  it("play", function() {
    var fundamental = 440;
    var noteList = [
      {
        "action": "noteOn",
        "noteName": "root",
        "change": {
          "carrier.freq": fundamental
        },
        "point" : [0,1,0],
        "synthIndex": 0

      },
      {
        "action": "noteOn",
        "noteName": "mediant",
        "change": {
            "carrier.freq": fundamental * 5/4
        },
        "point" : [1,2,0],
        "synthIndex": 0
      },
      {
        "action": "noteOn",
        "noteName": "dominant",
        "change": {
            "carrier.freq": fundamental * 3/2
        },
        "point" : [1,3,0],
        "synthIndex": 0
      },
      {
        "action": "noteOff",
        "noteName": "root",
        "synthIndex": 0
      },
      {
        "action": "noteOff",
        "noteName": "mediant",
        "synthIndex": 0
      },
      {
        "action": "noteOff",
        "noteName": "dominant",
        "synthIndex": 0
      }
    ];
    var synthSettingList = [{
      "synthDef": {
        "id": "carrier",
        "ugen": "flock.ugen.sin",
        "freq": fundamental,
        "mul": {
          "id": "env",
          "ugen": "flock.ugen.env.simpleASR",
          "attack": 0.25,
          "sustain": 1.0,
          "release": 0.5
        }
      }
    }];

    var score = new LAUGH.Score(noteList, synthSettingList);
    score.play();
  });
});

