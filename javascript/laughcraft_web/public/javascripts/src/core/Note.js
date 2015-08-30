var LAUGH;

(function (LAUGH) {
  var Note = function () {
    var Note = function (key, duration) {
      this.key = key;
      this.duration = duration;
    }

    return Note;
  }();
  LAUGH.Note = Note;
})(LAUGH || (LAUGH = {}));
