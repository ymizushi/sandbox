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

var Foo = function (text) {
    this.text = text;
}

var foo = new Foo('Hello, alert.');
alert(foo);
foo.toString = function () {
    return this.text;
}
alert(foo); // => Hello, alert. と表示される
console.log('foo bar');
console.log('hoge piyo');

// ダミーconsoleオブジェクト
if (!window.console) {
    (function (win) {
        var names = [
            'assert', 'clear', 'count', 'debug', 'dir', 'dirxml',
            'error', 'exception', 'group', 'groupCollapsed', 'groupEnd',
            'info', 'log', 'notifyFirebug', 'profileEnd', 
            'table', 'time', 'timeEnd', 'trace', 'warn'];
        var consoleMock = {};
        for (var i = 0, len = names.length; i < len; i++) {
            consoleMock[names[i]] = function () {};
        }
        win.console = consoleMock;
    }(window));
}
