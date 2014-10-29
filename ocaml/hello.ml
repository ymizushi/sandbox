(*
        let rec quicksort = function
          | [] -> []
          | pivot :: rest ->
              let is_less x = x < pivot in
              let left, right = List.partition is_less rest in
              quicksort left @ [pivot] @ quicksort right
    *)

let double f x = f (f x) in
let f x = x + 1 in
  double (double f) ;;

(*
 fn -> (int -> int)
    
*)


let double f x = f (f x) in
let f x = x + 1 in
  double (double f) ;;

let x  = "0" in 
 "abc" ^ x;;

let x = "oo" in
  "abc" ^ x ^ "def";;


let hoge = 
  let x = 1 in
    match x with
    0 -> "abb"
   |1 -> "baa"
   |_ -> "unexpected";;


print_string hoge


(* データ型を定義する *)
type white_or_black =   (* データ型の名前は小文字で始まる *)
    White of int        (* データ型の構成子は大文字で始まる *)
  | Black of string ;;
White 1;;
Black "abc";;
