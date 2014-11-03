(use 'clojure.test)

(defprotocol Evalable
  (evl [this]))
(defprotocol Findable
  (fnd [dict key]))

(deftype Token [s])
(deftype Atom [token])
(deftype Int [token]
  Evalable
  (evl [this]
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

(def input ["(" "def" "hoge" "1"])

(defn parse [tokens]
  (for [t tokens]

    )
  )

(defn tokenize [s] s)


(deftest test-Env []
  (testing "fnd"
    (let [env (Env. {:hoge (Token. "1")} nil)]
      (is (= (.s (fnd env :hoge)) "1")))))

(run-tests)
