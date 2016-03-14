"use strict";

var _typeof2 = typeof Symbol === "function" && typeof Symbol.iterator === "symbol" ? function (obj) { return typeof obj; } : function (obj) { return obj && typeof Symbol === "function" && obj.constructor === Symbol ? "symbol" : typeof obj; };

var _typeof = typeof Symbol === "function" && _typeof2(Symbol.iterator) === "symbol" ? function (obj) {
  return typeof obj === "undefined" ? "undefined" : _typeof2(obj);
} : function (obj) {
  return obj && typeof Symbol === "function" && obj.constructor === Symbol ? "symbol" : typeof obj === "undefined" ? "undefined" : _typeof2(obj);
};

var _createClass = function () {
  function defineProperties(target, props) {
    for (var i = 0; i < props.length; i++) {
      var descriptor = props[i];descriptor.enumerable = descriptor.enumerable || false;descriptor.configurable = true;if ("value" in descriptor) descriptor.writable = true;Object.defineProperty(target, descriptor.key, descriptor);
    }
  }return function (Constructor, protoProps, staticProps) {
    if (protoProps) defineProperties(Constructor.prototype, protoProps);if (staticProps) defineProperties(Constructor, staticProps);return Constructor;
  };
}();

function _possibleConstructorReturn(self, call) {
  if (!self) {
    throw new ReferenceError("this hasn't been initialised - super() hasn't been called");
  }return call && ((typeof call === "undefined" ? "undefined" : _typeof(call)) === "object" || typeof call === "function") ? call : self;
}

function _inherits(subClass, superClass) {
  if (typeof superClass !== "function" && superClass !== null) {
    throw new TypeError("Super expression must either be null or a function, not " + (typeof superClass === "undefined" ? "undefined" : _typeof(superClass)));
  }subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } });if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass;
}

function _classCallCheck(instance, Constructor) {
  if (!(instance instanceof Constructor)) {
    throw new TypeError("Cannot call a class as a function");
  }
}

var Time = function () {
  function Time(date) {
    _classCallCheck(this, Time);

    this._date = date;
  }

  _createClass(Time, [{
    key: "hours",
    get: function get() {
      return this._date.getHours();
    }
  }, {
    key: "minutes",
    get: function get() {
      return this._date.getMinutes();
    }
  }, {
    key: "seconds",
    get: function get() {
      return this._date.getSeconds();
    }
  }, {
    key: "time",
    get: function get() {
      return this._date.getTime();
    }
  }]);

  return Time;
}();

var Timer = function () {
  function Timer(time) {
    _classCallCheck(this, Timer);

    this._time = time;
  }

  _createClass(Timer, [{
    key: "tick",
    value: function tick() {
      return this.diff(new Time(new Date()));
    }
  }, {
    key: "diff",
    value: function diff(time) {
      return time.time - this._time.time;
    }
  }]);

  return Timer;
}();

var Listener = function Listener() {
  _classCallCheck(this, Listener);
};

var TimerListener = function (_Listener) {
  _inherits(TimerListener, _Listener);

  function TimerListener(timer) {
    _classCallCheck(this, TimerListener);

    var _this = _possibleConstructorReturn(this, Object.getPrototypeOf(TimerListener).call(this));

    _this._timer = timer;
    _this._clockComponent = new ClockComponent();
    _this._timerComponent = new TimerComponent();
    _this._lapComponents = [];
    return _this;
  }

  _createClass(TimerListener, [{
    key: "tick",
    value: function tick() {
      this._timer.tick();
      this._clockComponent.tick(this._timer);
    }
  }, {
    key: "lap",
    value: function lap() {
      this._lapComponents.forEach(function (e) {
        return e.lap();
      });
    }
  }]);

  return TimerListener;
}(Listener);

var Component = function Component() {
  _classCallCheck(this, Component);
};

var ClockComponent = function (_Component) {
  _inherits(ClockComponent, _Component);

  function ClockComponent() {
    _classCallCheck(this, ClockComponent);

    return _possibleConstructorReturn(this, Object.getPrototypeOf(ClockComponent).apply(this, arguments));
  }

  _createClass(ClockComponent, [{
    key: "tick",
    value: function tick(timer) {
      this._draw(timer);
    }
  }, {
    key: "_draw",
    value: function _draw(timer) {
      var element = document.getElementById('clock');
      element.innerHTML = timer.hours + "時" + timer.minutes + "分" + timer.seconds + "秒";
    }
  }]);

  return ClockComponent;
}(Component);

var TimeComponent = function (_Component2) {
  _inherits(TimeComponent, _Component2);

  function TimeComponent() {
    _classCallCheck(this, TimeComponent);

    var _this3 = _possibleConstructorReturn(this, Object.getPrototypeOf(TimeComponent).call(this));

    _this3._beforeTime = new Timer(new Date());
    return _this3;
  }

  _createClass(TimeComponent, [{
    key: "lap",
    value: function lap(timer) {
      var millisec = this._beforeTime.diff(timer);
      this._beforeTime = timer;
      this._draw(millisec);
    }
  }, {
    key: "_draw",
    value: function _draw(millisec) {
      var time = document.getElementById('time');
      time.innerHTML = millisec;
    }
  }]);

  return TimeComponent;
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
  var timerListener = new TimerListener(new Timer(new Time(new Date())), new ClockComponent());
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

//# sourceMappingURL=main-compiled.js.map

//# sourceMappingURL=main-compiled-compiled.js.map