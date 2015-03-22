(ns hoge)

(defprotocol Evalable
  (evaluate [_ env]))

(defprotocol Drawable
  (draw [_ env]))

(deftype Symbol [token])

(extend-type Symbol
  Drawable
  (draw [_ env] (print "hoge"))
  Evalable
  (evaluate [_ env]
    (println (+ 1 1))))

(extend-type Symbol
  Drawable
    (draw [_ env] (print "piyo")))

(draw (Symbol. "hoge") "hoge")
