(use 'clojure.test)
(require '[clojure.string :as str])

(defprotocol Evalable
  (evl [_]))
(defprotocol Findable
  (fnd [_ key]))

(deftype Token [s])
(deftype Atom [token])
(deftype Int [token]
  Evalable
  (evl [_]
    (int token)))

(deftype Env [dic outer]
  Evalable
  Findable
  (fnd [_ key]
    (if-let [value (get dic key)]
      value
      (if-let [value (fnd outer key)]
        value
        nil))))


(def input-string "(defn hoge [x y] (+ x y)")

(defn parse [tokens]
  (for [t tokens]

    )
  )

(defn tokenize [s] 
  (str/split s #"\s")
  )

(deftest test-tokenize []
  (testing "tokenize"
    (let [input "(defn hoge [x y] (+ x y))"]
      (is (= input ["(" "defn" "hoge" "[" "x" "y" "]" "(" "+" "x" "y" ")" ")"])))))

(deftest test-Env []
  (testing "fnd"
    (let [env (Env. {:hoge (Token. "1")} nil)]
      (is (= (.s (fnd env :hoge)) "1")))))

(run-tests)
