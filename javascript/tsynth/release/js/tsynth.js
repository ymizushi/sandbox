/// <reference path="../typings/webaudioapi/waa.d.ts" />
/// <reference path="../typings/rx/rx.d.ts" />
var tsynth;
(function (tsynth) {
    var Sequencer = (function () {
        function Sequencer(noteList) {
            this.noteList = noteList;
        }
        Sequencer.prototype.play = function () {
        };
        return Sequencer;
    })();
    var Note = (function () {
        function Note() {
        }
        return Note;
    })();
    var Synth = (function () {
        function Synth() {
        }
        return Synth;
    })();
    var AudioCtx = (function () {
        function AudioCtx(window) {
            this.audioContext = new window.AudioContext();
        }
        AudioCtx.prototype.createOscillator = function () {
            return this.audioContext.createOscillator();
        };
        AudioCtx.prototype.createGain = function () {
            return this.audioContext.createGain();
        };
        AudioCtx.prototype.getDestination = function () {
            return this.audioContext.destination;
        };
        return AudioCtx;
    })();
    var Main = (function () {
        function Main() {
        }
        Main.test = function (window) {
            if (!window.File || !window.FileReader || !window.FileList || !window.Blob) {
                alert('The File APIs are not fully supported in this browser.');
            }
            var buffer = new ArrayBuffer(4 + 2 + 4);
            var view = new DataView(buffer);
            var offset = 0;
            // 4byteの書き込み
            view.setUint16(offset, 0x0001, true);
            offset += 2;
            view.setUint16(offset, 0x0100, true);
            offset += 2;
            // 2byteの書き込み
            view.setUint8(offset, 0xff);
            offset += 1;
            view.setUint8(offset, 0x0f);
            offset += 1;
            // 4byteの書き込み
            view.setInt16(offset, -50, true);
            offset += 2;
            view.setUint16(offset, -30, true);
            offset += 2;
            var result = new Uint8Array(buffer);
            console.log(result); // =>  [1, 0, 0, 1, 255, 15, 206, 255, 226, 255]
        };
        Main.start = function (window) {
            var handleFileSelect = function handleFileSelect(evt) {
                var files = evt.target.files; // FileList object
                for (var i = 0, f; f = files[i]; i++) {
                    // Only process image files.
                    if (!f.type.match('image.*')) {
                        continue;
                    }
                    var reader = new FileReader();
                    // Closure to capture the file information.
                    reader.onload = (function (theFile) {
                        return function (e) {
                            // Render thumbnail.
                            var span = document.createElement('span');
                            span.innerHTML = ['<img class="thumb" src="', e.target.result, '" title="', theFile.name, '"/>'].join('');
                            document.getElementById('list').insertBefore(span, null);
                        };
                    })(f);
                    // Read in the image file as a data URL.
                    reader.readAsArrayBuffer(f);
                }
                console.log(files);
            };
            Main.test(window);
            var midiFile = document.getElementById('midi_file');
            midiFile.addEventListener('change', handleFileSelect, false);
            var context = new AudioCtx(window);
            var oscillator = context.createOscillator();
            oscillator.frequency.value = 300;
            var gain = context.createGain();
            oscillator.connect(gain);
            gain.connect(context.getDestination());
            oscillator.start(0);
            var noteList = [new Note(), new Note()];
            var sequencer = new Sequencer(noteList);
            sequencer.play();
            window.setTimeout(function () {
                oscillator.stop(0);
            }, 5000);
            var clickStream = Rx.Observable.fromEvent(document, "mouseup");
            clickStream.buffer(clickStream.throttleFirst(250)).map(function (x) {
                return x.length;
            }).filter(function (n) {
                return n >= 2;
            }).subscribe(function (n) {
                console.log(n + "click");
            });
        };
        return Main;
    })();
    Main.start(window);
})(tsynth || (tsynth = {}));
