class Time {
  constructor(date) {
    this._date = date;
  }

  get hours() {
    return this._date.getHours();
  }

  get minutes() {
    return this._date.getMinutes();
  }

  get seconds() {
    return this._date.getSeconds();
  }

  get time() {
    return this._date.getTime();
  }
}


class Timer {
  constructor(time) {
    this._time = time;
  }

  init() {
    this._time = new Time(new Date());
  }

  tick () {
    return this.diff(new Time(new Date()));
  }

  diff(time) {
    return time.time - this._time.time
  }
}

class Listener {}

class TimerListener extends Listener {
  constructor(timer) {
    super()
    this._timer = timer;
    this._clockComponent = new ClockComponent();
    this._timeComponent = new TimeComponent();
    this._lapComponents = [];
  }

  tick() {
    this._timer.tick();
    this._clockComponent.tick(this._timer);
  }

  stop() {
    this._timeComponent.stop(this._timer);
  }

  start() {
    this._timeComponent.start(this._timer);
  }

  lap() {
    this._lapComponents.forEach((e) => e.lap());
  }
}

class Component {
}

class ClockComponent extends Component {
  tick(timer) {
    this._draw(timer);
  }

  _draw(timer) {
    var element = document.getElementById('clock');
    element.innerHTML=timer.hours + "時" + timer.minutes + "分" + timer.seconds + "秒";
  }

}

class TimeComponent extends Component {
  constructor() {
    super();
    this._beforeTime = new Timer(new Date());
  }

  lap(timer) {
    const millisec = this._beforeTime.diff(timer);
    this._beforeTime = timer;
    this._draw(millisec);
  }

  _draw(millisec) {
    var time = document.getElementById('time');
    time.innerHTML = millisec;
  }
}

class EventHandler {
  constructor() {
    this.listeners = [];
  }

  addListener(listener) {
    this.listeners.push(listener);
  }

  notify() {
    for (var i in this.listeners) {
      this.listeners[i].notify();
    }
  }

  stopTime() {
    for (var i in this.listeners) {
      this.listeners[i].stopTime();
    }
  }
}

function main() {
  const eventHandler = new EventHandler();
  const timerListener = new TimerListener(new Timer(new Time(new Date())), new ClockComponent());
  eventHandler.addListener(timerListener);

  window.onload=function(){
    document.getElementById('start').addEventListener('click', () => {
			console.log("start");
    });
    document.getElementById('lap').addEventListener('click', () => {
			console.log("lap");
    });
    document.getElementById('stop').addEventListener('click', () => {
			console.log("stop");
    });

		window.setInterval(() => eventHandler.notify(), 1000);
	}

}

main();
