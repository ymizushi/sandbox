var LAUGH;
(function (LAUGH) {
  // CameraCreator
  var CameraCreator = function () {
    var CameraCreator = function (framework) {
      this._framework = framework;
    };

    CameraCreator.prototype.create = function (left, right, top, bottom, shortLength, longLength) {
      var camera = new this._framework.OrthographicCamera(left, right, top, bottom, shortLength, longLength)
      return new Camera(camera);
    
    };
    
    return CameraCreator;
  }();
  LAUGH.CameraCreator = CameraCreator;

  // Camera
  var Camera = function () {
    var Camera = function (framework) {
      this._framework = framework;
    };

    Camera.prototype.setPoint = function (point) {
      this._framework.position.x = point.x;
      this._framework.position.y = point.y;
      this._framework.position.z = point.z;
    }

    return Camera;
  }();
  LAUGH.Camera = Camera;

})(LAUGH || (LAUGH = {}));
