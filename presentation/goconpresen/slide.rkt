#lang slideshow
(require slideshow/code)
(require slideshow/step)
 
(slide
 (item "github APIをAndroidから使ってみた"))

(slide
  #:title "自己紹介"
  (item "ニコニコ生放送開発セクション")
  (item "2013年7月1日入社" )
  (subitem "去年のハッカソンが入社日"))

(slide
  #:title "今年のテーマ"
  (item "出会い")
  'next
  (item "出会いといえば")
  'next
  (bt "合コン"))

(slide
  #:title "合コン"
  (item "合コンとドワンゴ")
  'next
   (bitmap "gocon.jpg")
    (item "https://twitter.com/berotti3/status/482531967322185729"))

(slide
  #:title "目指すもの"
  (item "githubアカウントでLINEみたいなものを作る"))

(slide
  #:title "とりあえず出来た"
  (item "gist APIを叩いてgistコメントの取得・投稿が出来る"))
(slide
  (item "デモ"))

(slide
  (item "ちなみに"))

(slide
  #:title "合コンの結果"
  'next
  'alts
  (list (list (bitmap "gocon1.jpg"))
        (list (bitmap "gocon2.jpg"))))

(slide
  (item "ご清聴ありがとうございました"))