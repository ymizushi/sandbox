var LAUGH;
(function (LAUGH) {
  var Score = function () {
    var Score = function (scoreJson) {
      this.scoreJson = scoreJson;
    };

    Score.prototype.play = function () {
      var synthList = this.scoreJson["synthList"];
      var polySynthList = [];
      for (var i=0; i<this.synthList.length; i++) {
        var polySynth = flock.synth.polyphonic(synthList[i]);
        polySynthList.push(polySynth);
      }

      var clock = flock.scheduler.async();
      var noteList = this.scoreJson["noteList"];
      var idx = 0;
      clock.repeat(1, function () {
          if (idx >= noteList.length) {
            idx = 0;
          }
          var event = noteList[idx];
          polySynthList[event.synthIndex][event.action](event.noteName, event.change);
          idx++;
      });
      flock.enviro.shared.play();
    };

    Score.prototype.getNoteList = function () {
      return this.scoreJson.noteList;
    };

    Score.prototype.getSynthList = function() {
      return this.scoreJson.synthList;
    };

    Score.prototype.getObjectList = function() {
      return this.scoreJson.objectList;
    };

    Score.prototype.getKeyframeList = function() {
      return this.scoreJson["keyframeList"];
    };
    return Score;
  }();
  LAUGH.Score = Score;
})(LAUGH || (LAUGH = {}));






