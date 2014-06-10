(use 'clojure.test)

(defn hoge [] (+ 1 2))

(deftest test-add []
  (testing "add"
    (is (= 2 (+ 1 1)))
    (is (= 3 (hoge)))
    )) 
(run-tests)
