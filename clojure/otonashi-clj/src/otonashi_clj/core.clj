(ns otonashi-clj.core)

(use 'overtone.live)

(defn foo [freq]
  (pan2 (sin-osc freq)))
 
; ドレミの周波数を定義
(def doremi {:none 0
             :do  261.6
             :re  293.6
             :mi  329.6
             :fa  349.2
             :so  392
             :ra  440
             :si  493.8
             :do2 523.3
             :re2 587})
 
(defn key-on [note]
  (demo 0.3 (foo (note doremi))))
 
(defn play-notes [notes]
  (dorun (map #(do (key-on %) (Thread/sleep 300))
              notes)))
 
;ジングルベル
(defn play-jingle-bells []
  (play-notes
   [:do :ra :so :fa :do :none
    :do :ra :so :fa :re :none
    :re :si :ra :so :mi :none
    :do2 :do2 :si :so :ra :none
 
    :do :ra :so :fa :do :none
    :do :ra :so :fa :re :none
    :re :si :ra :so :do2 :do2 :do2 :do2
    :re2 :do2 :si :ra :so :none
 
    :do2 :none
    :ra :ra :ra :none :ra :ra :ra :none
    :ra :do2 :fa :so :ra :none
    :si :si :si :si :si :ra :ra :ra
    :ra :so :so :ra :so :none
 
    :do2 :none
    :ra :ra :ra :none :ra :ra :ra :none
    :ra :do2 :fa :so :ra :none
    :si :si :si :si :si :ra :ra :ra
    :do2 :do2 :si :so :fa
    ])
)

(def notes
  {:C1  {:num 36 :fre 65.4}
   :C#1 {:num 37 :fre 69.3}
   :D1   {:num 38 :fre 73.4}
   :D1#  {:num 39 :fre 77.8}
   :E1   {:num 40 :fre 82.4}
   :F1   {:num 41 :fre 87.3}
   :F#1  {:num 42 :fre 92.5}
   :G1   {:num 43 :fre 98.0}
   :G#1  {:num 44 :fre 103.8}
   :A1   {:num 45 :fre 110.0}
   :A#1  {:num 46 :fre 116.5}
   :B1   {:num 47 :fre 123.5}
   :C2   {:num 48 :fre 130.8}
   :CS2  {:num 49 :fre 138.6}
   }
  )

(defn key-on [note]
  (demo 0.3 (foo (note doremi))))
 
(defn play-notes [notes]
  (dorun (map #(do (key-on %) (Thread/sleep 300)) notes)))

(defn -main []
  (play-jingle-bells))
