var LAUGH;
(function (LAUGH) {
  var ScoreLoader = function () {
    var ScoreLoader = function () {};

    ScoreLoader.prototype.load = function (scoreId) {
      var scoreRequestor = new LAUGH.JsonRequestor();
      var url = "projects/" + scoreId.toString() + ".json"
      var scoreJson = scoreRequestor.fetch(url);
      return new LAUGH.Score(scoreJson);
    };
    return ScoreLoader;
  }();
  LAUGH.ScoreLoader = ScoreLoader;
})(LAUGH || (LAUGH = {}));
