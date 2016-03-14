"use strict";

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

var Timer = function () {
  function Timer(date) {
    _classCallCheck(this, Timer);

    this.init(date);
  }

  _createClass(Timer, [{
    key: "init",
    value: function init(date) {
      this.hours = date.getHours();
      this.minutes = date.getMinutes();
      this.seconds = date.getSeconds();
    }
  }, {
    key: "tick",
    value: function tick() {
      var date = new Date();
      this.hours = date.getHours();
      this.minutes = date.getMinutes();
      this.seconds = date.getSeconds();
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

  function TimerListener(timer, timeComponent) {
    _classCallCheck(this, TimerListener);

    var _this = _possibleConstructorReturn(this, Object.getPrototypeOf(TimerListener).call(this));

    _this.timer = timer;
    _this.component = component;
    return _this;
  }

  _createClass(TimerListener, [{
    key: "notify",
    value: function notify() {
      this.timer.tick();
      this.component.update(this.timer);
    }
  }, {
    key: "stopTime",
    value: function stopTime() {
      this.component.update(this.timer);
    }
  }]);

  return TimerListener;
}(Listener);

var Component = function Component() {
  _classCallCheck(this, Component);
};

var TimerComponent = function (_Component) {
  _inherits(TimerComponent, _Component);

  function TimerComponent() {
    _classCallCheck(this, TimerComponent);

    return _possibleConstructorReturn(this, Object.getPrototypeOf(TimerComponent).apply(this, arguments));
  }

  _createClass(TimerComponent, [{
    key: "update",
    value: function update(timer) {
      this.draw(timer);
    }
  }, {
    key: "draw",
    value: function draw(timer) {
      var element = document.getElementById('clock');
      element.innerHTML = timer.hours + "時" + timer.minutes + "分" + timer.seconds + "秒";
    }
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
      for (var i in this.listeners) {
        this.listeners[i].notify();
      }
    }
  }, {
    key: "stopTime",
    value: function stopTime() {
      for (var i in this.listeners) {
        this.listeners[i].stopTime();
      }
    }
  }]);

  return EventHandler;
}();

function main() {
  var eventHandler = new EventHandler();
  var timerListener = new TimerListener(new Timer(new Date()), new TimerComponent());
  eventHandler.addListener(timerListener);

  window.onload = function () {
    document.getElementById('start').addEventListener('click', function () {
      console.log("start");
    });
    document.getElementById('lap').addEventListener('click', function () {
      console.log("lap");
    });
    document.getElementById('stop').addEventListener('click', function () {
      console.log("stop");
    });

    window.setInterval(function () {
      return eventHandler.notify();
    }, 1000);
  };
}

main();