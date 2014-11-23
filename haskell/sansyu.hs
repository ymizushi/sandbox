lucky:: Int -> String
lucky y = "Lucky NUMBER SEEVEN"

sayMe :: Int -> String
sayMe 1 = "One!"
sayMe 2 = "Two"
sayMe 3 = "Three"

factorial :: Int -> Int
factorial 0 = 1
factorial n = n * factorial (n-1)


hoge x y = x + y



main = 
    print(sayMe 3)
