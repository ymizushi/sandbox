class Timer{
  constructor(date) {
    this.hours = date.getHours();
    this.minutes = date.getMinutes();
    this.seconds = date.getSeconds();
  }

  get toString() {
    return this.hours.toString() + this.minutes.toString() + this.seconds().toString();
  
  }

  tick () {
    const date = new Date();
    this.hours = date.getHours();
    this.minutes = date.getMinutes();
    this.seconds = date.getSeconds();
    return this;
  }
}

class Listener {
  notify() {
  }
}

class TimerListener extends Listener {
  constructor(timer, component) {
    super()
    this.timer = timer;
    this.component = component
  }

  notify() {
    this.component.update(this.timer)
  }
} 

class Component {
  constructor(width, height) {
    this.width = width;
    this.height = height;
  }
  update(width ,height) {
    this.width = width;
    this.height = height;
  }
}

class TimerComponent extends Component {
  constructor(width, height) {
    super(width, height);
  }

  draw(ctx) {
    var element = window.getElementById("clockstr"");
  
  }
}


class EventHandler {
  constructor() {
    this.listeners = [];
  }

  addListener(listener) {
    this.listeners.push(listener)
  }

  notify() {
    for (var n of this.listeners) {
      n.notify()
    }
  }
}

function main() {
  const eventHandler = new EventHandler();
  const timerListener = new TimerListener(new Timer(new Date()), new Component(100, 200))
  eventHandler.addListener(timerListener);

  window.setInteval(eventHandler.notify, 1000);

  window.onLoad = function () {
    const canvas = document.getElementById('clock');
    if (canvas == null) {
      console.log("canvas context is null");
    }
    const ctx = canvas.getContext("2d");
    ctx.fillStyle = "rgb(200,0,0)";
    ctx.fillRect (10, 10, 55, 50);

    ctx.fillStyle = "rgba(0, 0, 200, 0.5)";
    ctx.fillRect (30, 30, 55, 50);
  }
}

main();
