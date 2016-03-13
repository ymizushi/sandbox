"use strict";

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

var Timer = function () {
  function Timer(date) {
    _classCallCheck(this, Timer);

    this.hours = date.getHours();
    this.minutes = date.getMinutes();
    this.seconds = date.getSeconds();
  }

  _createClass(Timer, [{
    key: "tick",
    value: function tick() {
      var date = new Date();
      this.hours = date.getHours();
      this.minutes = date.getMinutes();
      this.seconds = date.getSeconds();
      return this;
    }
  }, {
    key: "toString",
    get: function get() {
      return this.hours.toString() + this.minutes.toString() + this.seconds().toString();
    }
  }]);

  return Timer;
}();

var Listener = function () {
  function Listener() {
    _classCallCheck(this, Listener);
  }

  _createClass(Listener, [{
    key: "notify",
    value: function notify() {}
  }]);

  return Listener;
}();

var TimerListener = function (_Listener) {
  _inherits(TimerListener, _Listener);

  function TimerListener(timer, component) {
    _classCallCheck(this, TimerListener);

    var _this = _possibleConstructorReturn(this, Object.getPrototypeOf(TimerListener).call(this));

    _this.timer = timer;
    _this.component = component;
    return _this;
  }

  _createClass(TimerListener, [{
    key: "notify",
    value: function notify() {
      this.component.update(this.timer);
    }
  }]);

  return TimerListener;
}(Listener);

var Component = function () {
  function Component(width, height) {
    _classCallCheck(this, Component);

    this.width = width;
    this.height = height;
  }

  _createClass(Component, [{
    key: "update",
    value: function update(width, height) {
      this.width = width;
      this.height = height;
    }
  }]);

  return Component;
}();

var TimerComponent = function (_Component) {
  _inherits(TimerComponent, _Component);

  function TimerComponent(width, height) {
    _classCallCheck(this, TimerComponent);

    return _possibleConstructorReturn(this, Object.getPrototypeOf(TimerComponent).call(this, width, height));
  }

  _createClass(TimerComponent, [{
    key: "draw",
    value: function draw(ctx) {}
  }]);

  return TimerComponent;
}(Component);

var EventHandler = function () {
  function EventHandler() {
    _classCallCheck(this, EventHandler);

    this.listeners = [];
  }

  _createClass(EventHandler, [{
    key: "addListener",
    value: function addListener(listener) {
      this.listeners.push(listener);
    }
  }, {
    key: "notify",
    value: function notify() {
      var _iteratorNormalCompletion = true;
      var _didIteratorError = false;
      var _iteratorError = undefined;

      try {
        for (var _iterator = this.listeners[Symbol.iterator](), _step; !(_iteratorNormalCompletion = (_step = _iterator.next()).done); _iteratorNormalCompletion = true) {
          var n = _step.value;

          n.notify();
        }
      } catch (err) {
        _didIteratorError = true;
        _iteratorError = err;
      } finally {
        try {
          if (!_iteratorNormalCompletion && _iterator.return) {
            _iterator.return();
          }
        } finally {
          if (_didIteratorError) {
            throw _iteratorError;
          }
        }
      }
    }
  }]);

  return EventHandler;
}();

function main() {
  var eventHandler = new EventHandler();
  var timerListener = new TimerListener(new Timer(new Date()), new Component(100, 200));
  eventHandler.addListener(timerListener);

  window.setInteval(eventHandler.notify, 1000);

  window.onLoad = function () {
    var canvas = document.getElementById('clock');
    if (canvas == null) {
      console.log("canvas context is null");
    }
    var ctx = canvas.getContext("2d");
    ctx.fillStyle = "rgb(200,0,0)";
    ctx.fillRect(10, 10, 55, 50);

    ctx.fillStyle = "rgba(0, 0, 200, 0.5)";
    ctx.fillRect(30, 30, 55, 50);
  };
}

main();