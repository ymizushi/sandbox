function audioTest() {
    var context = new webkitAudioContext();
    // サンプリングレートを48KHzに設定
    context.sampleRate = 48000;

    // モノラル/48KHz/48000サンプルのAudioBufferを作成
    var buf = context.createBuffer(1, 48000, 48000);

    // データが格納されている配列を取得
    var data = buf.getChannelData(0);

    var i;

    // 配列に音声データを書き込む
    for (i = 0;i < data.length;i++) {
        if ((i % 100) < 50) {
            data[i] = 0.5;
        } else {
            data[i] = -0.5;
        }
    }

    // AudioSourceを作成
    var src = context.createBufferSource();

    // AudioSourceに作成した音声データを設定
    src.buffer = buf;

    // 出力先を設定
    src.connect(context.destination);

    // 出力開始
    src.noteOn(0);
}
