#lang slideshow
(require slideshow/code)
(require slideshow/step)
 
(slide
 (item "Javascriptで処理系を作ってみたよ"))

(slide
  #:title "自己紹介"
  (item "某ネットに生まれて、ネットでつながる企業勤務")
  (item "好きなもの"
      (subitem "ブラック企業")))

(slide
  #:title "Emola"
  (item "Emotional Hubというサービス（現在鋭意開発中）で使用する言語")
  (item "特徴"
    (item "Lisp"
      (item "(Clojure+Racket)/2"))
    (item "https://github.com/ymizushi/emohub")))

(slide
  (item "デモ"))

(slide
  #:title "今後実装する機能"
  (item "グラフィカルな構文リスト編集")
  (item "サウンドシーケンス・シンセサイズ機能"
    (subitem "サウンドシーケンス構文")
    (subitem "構文リスト自体に音のメタ情報を持たせる")))

(slide
  (item "ご清聴ありがとうございました"))
