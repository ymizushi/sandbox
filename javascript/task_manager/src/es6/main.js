class Timer{
  constructor(date) {
    this.init(date);
  }

  init(date) {
    this.date = date;
    this.hours = date.getHours();
    this.minutes = date.getMinutes();
    this.seconds = date.getSeconds();
  }

  tick () {
    const date = new Date();
    this.hours = date.getHours();
    this.minutes = date.getMinutes();
    this.seconds = date.getSeconds();
  }

  diff(date) {
    return date.getTime() - this.date.getTime();
  }
}

class Listener {
  notify() {
  }
}

class TimerListener extends Listener {
  constructor(timer, timeComponent) {
    super()
    this.timer = timer;
    this.component = component
		this.timeComponent = 
  }

  notify() {
    this.timer.tick();
    this.component.update(this.timer);
  }

  stopTime() {
    this.component.update(this.timer);
  }
} 

class Component {
}

class ClockComponent extends Component {
  update(timer) {
    this.draw(timer);
  }

  draw(timer) {
    var element = document.getElementById('clock');
    element.innerHTML=timer.hours + "時" + timer.minutes + "分" + timer.seconds + "秒";
  }

}

class TimeComponent extends Component {
  constructor() {
    this.beforeTime = new Timer(new Date());
  }

  update(timer) {
    this.beforeTime = timer
    this.draw(timer);
  }

  draw(timer) {
    var time = document.getElementById('time');
    time.innerHTML=timer.hours + "時" + timer.minutes + "分" + timer.seconds + "秒";
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
  const timerListener = new TimerListener(new Timer(new Date()), new ClockComponent());
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
