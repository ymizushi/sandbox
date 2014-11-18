fac:: Int -> Int
fac n =
  if n == 1 then
    1
  else
    n * fac(n-1)

reverse:: String -> String
reverse input output =
  if input == "" then
    output
  else
    let first = head input
    let rest = tail input
    reverse rest output++first

hoge:: Int -> Int -> Int
hoge x y = x + y
main = 
    print (fac 5)
