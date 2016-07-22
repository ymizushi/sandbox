let double f x = f (f x) in
let f x = x + 1 in
  double (double f) ;;

let rec fact n =
  if n = 0 then
    1
  else
    n * fact (n - 1)

print_int fact(5)
