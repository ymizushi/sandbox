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

(deftest test-Env []
  (testing "fnd"
    (is (= (fnd (Env. {:hoge (Token. "1")} nil) :hoge)
           (Token. "1"))))) 

(run-tests)
