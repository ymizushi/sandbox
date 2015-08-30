var LAUGH;
(function (LAUGH) {
  var Synth = function () {
    var Synth = function (synthName, setting) {
      this._synthName = setting;
      this._setting = setting;
      this._flock = flock;
    };

    Synth.prototype.synth = flock.synth;

    Synth.prototype.play = function (time) {
      this.synth(this._setting);
      this._flock.enviro.shared.play();
    };

    Synth.prototype.stop = function () {};

    Synth.prototype.get = function(typeName) {
      this._flock.get(typeName);
    };

    Synth.prototype.set = function(input, rate) {
      this._flock.set(input, rate);
    };
    return Synth;
  }();
  LAUGH.Synth = Synth;
})(LAUGH || (LAUGH = {}));
