(*
let rec quicksort = function
  | [] -> []
  | pivot :: rest ->
      let is_less x = x < pivot in
      let left, right = List.partition is_less rest in
      quicksort left @ [pivot] @ quicksort right
*)

(*
        let f x = x + 1 in
          print_int(f (f 3));;
    *)


let rec gcd x y = 
  if x = y then
    x
  else
    if x > y then
      gcd (x-y) y
    else
      gcd x (y-x)

let hoge x = 
  x

let _ =
  print_int (gcd 5 15);;
