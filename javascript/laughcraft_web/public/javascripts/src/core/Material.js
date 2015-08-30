var LAUGH;
(function (LAUGH) {

  // GraphicContext
  var GraphicContext = function () {
    var GraphicContext = function (framework) {
      this._framework = framework;
    };

    GraphicContext.prototype.drawPoint = function (point) { };

    GraphicContext.prototype.drawLine = function (line) { };

    GraphicContext.prototype.drawCircle = function (circle) { };

    GraphicContext.prototype.drawCube = function (cube) { };

    return GraphicContext;
  }();
  LAUGH.GraphicContext = GraphicContext;

  // Point
  var Point = function () {
    var Point = function (x, y, z) {
      this.x = x;
      this.y = y;
      this.z = z;
    };

    Point.prototype.draw = function (graphicContext) {
      graphicContext.drawPoint(this);
    };

    return Point;
  }();
  LAUGH.Point = Point;

  // Line
  var Line = function () {
    var Line = function (startPoint, endPoint) {
      this.startPoint = startPoint;
      this.endPoint = endPoint;
    };

    Line.prototype.draw = function (graphicContext) {
      graphicContext.drawLine(this);
    };
    return Line;
  }();
  LAUGH.Line = Line;

  // Circle
  var Circle = function () {
    var Circle = function (startPoint, endPoint) {
      this.startPoint = startPoint;
      this.endPoint = endPoint;
    };

    Circle.prototype.draw = function (graphicContext) {
      graphicContext.drawCircle(this);
    };
    return Circle;
  }();
  LAUGH.Circle = Circle;

  // Cube
  var Cube = function () {
    var Cube = function (startPoint, endPoint) {
      this.startPoint = startPoint;
      this.endPoint = endPoint;
    };

    Cube.prototype.draw = function (graphicContext) {
      graphicContext.drawCube(this);
    };
    return Cube;
  }();
  LAUGH.Cube = Cube;

})(LAUGH || (LAUGH = {}));

