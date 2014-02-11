// var a = document.getElementById('a');
// alert(a !== null); // => true
// var b = document.getElementById('b');
// alert(b !== null); //  true
// 
// window.onload = function () { alert('hello'); }
// document.addEventListener('DOMContentLoaded', function () {
//     alert('hello');
// }, false);
// 
//動的ロード
// var script = document.createElement('script');
// script.src = 'other-javascript.js';
// document.getElementByTagName('head')[0].appendChild(script);
//

onload = function() {
  draw1();
};
/* fillRect()の例 */
function draw1() {
  var canvas = document.getElementById('c1');
  if ( ! canvas || ! canvas.getContext ) { return false; }
  var ctx = canvas.getContext('2d');
  var x = 0;
  var y = 0;
  var before_x = 0;
  var before_y = 0;
  var b = 1.1;
  var r;
  var index = 100
  // for (var angle=0;angle< 360;angle++) {
    for (var theta=30;theta<50;theta=theta+0.2) {
      // ctx.clearRect();
      r = Math.pow(b, theta);
      x = r*Math.cos(theta);
      y = r*Math.sin(theta);
      ctx.beginPath();
      ctx.moveTo(index+before_x, index+before_y);
      ctx.lineTo(index+x, index+y);
      ctx.strokeStyle = "#df4b26";
      ctx.lineWidth = 3;
      ctx.stroke();
      before_x = x;
      before_y = y;
      console.log(theta);
    }
  //}
}







var Foo = function (text) {
    this.text = text;
}

// var foo = new Foo('Hello, alert.');
// alert(foo);
// foo.toString = function () {
//     return this.text;
// }
// alert(foo); // => Hello, alert. と表示される
// console.log('foo bar');
// console.log('hoge piyo');
// 
// // ダミーconsoleオブジェクト
// if (!window.console) {
//     (function (win) {
//         var names = [
//             'assert', 'clear', 'count', 'debug', 'dir', 'dirxml',
//             'error', 'exception', 'group', 'groupCollapsed', 'groupEnd',
//             'info', 'log', 'notifyFirebug', 'profileEnd', 
//             'table', 'time', 'timeEnd', 'trace', 'warn'];
//         var consoleMock = {};
//         for (var i = 0, len = names.length; i < len; i++) {
//             consoleMock[names[i]] = function () {};
//         }
//         win.console = consoleMock;
//     }(window));
// }
// 
// // document.getElementById('a').value="var";
// alert("hoge")

