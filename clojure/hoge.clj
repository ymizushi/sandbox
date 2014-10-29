(use 'clojure.test)

(defn compose [f g x]
  (f (g x)))

(let [f #(+ % 1)
      g #(* % 3)]
  (compose f g 10))
