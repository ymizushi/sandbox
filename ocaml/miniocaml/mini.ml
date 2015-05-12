type exp = IntLit of int
  |Plus of exp * exp
  |Minus of exp * exp
  |Div  of exp * exp
  |Mul  of exp * exp
  |Times of exp * exp
  |BoolLit of bool
  |If of exp * exp * exp
  |Eq of exp * exp;;

type value = 
  |IntVal of int
  |BoolVal of bool

let rec eval1 e = 
  match e with
    |IntLit(n) -> n
    |Plus(e1, e2) -> (eval1 e1) + (eval1 e2)
    |Times(e1, e2) -> (eval1 e1) * (eval1 e2)
    |Div(e1, e2) -> (eval1 e1) / (eval1 e2)
    |Mul(e1, e2) -> (eval1 e1) * (eval1 e2)
    |_ -> failwith "unknown expression";;

let rec eval2 e = 
  match e with
    |IntLit(n) -> IntVal(n)
    |Plus(e1, e2) ->
      binap 1 e1 e2
    |Times(e1, e2) -> 
      binap 2 e1 e2
    |Div(e1, e2) -> 
        begin
          match (eval2 e1, eval2 e2) with
            |(IntVal(n1), IntVal(n2)) -> IntVal(n1*n2)
            |_ -> failwith "integer values expected"
        end
    |Mul(e1, e2) -> 
        begin
          match (eval2 e1, eval2 e2) with
            |(IntVal(_), IntVal(0)) -> failwith "0 divide is not accepted"
            |(IntVal(n1), IntVal(n2)) -> IntVal(n1/n2)
            |_ -> failwith "integer values expected"
        end
    |If(e1, e2, e3) -> 
        begin
          match (eval2 e1) with
            |BoolVal(true) ->  (eval2 e2)
            |BoolVal(false) -> (eval2 e3)
            |_ -> failwith "integer values expected"
        end
    |_ -> failwith "unknown expression"
and binap flag e1 e2 = 
  match (eval2 e1, eval2 e2) with
  |(IntVal(n1), IntVal(n2)) ->
    if flag = 1 then IntVal(n1+n2)
    else IntVal(n1*n2)
  |_ -> failwith "integer values expected"

let print_intval value = match value with
    |IntVal(i) -> print_int i 
    |BoolVal(true) -> print_int 1
    |BoolVal(false) -> print_int 0;;

let rec eval2b e =
  let binop f e1 e2 = 
    match (eval2b e1, eval2b e2) with
    |(IntVal(n1), IntVal(n2)) -> IntVal(f n1 n2)
    |_ -> failwith "integer values expected"
    in
      match e with 
      |IntLit(n) -> IntVal(n)
      |Plus(e1, e2) -> binop (+) e1 e2
      |Times(e1, e2) -> binop ( * ) e1 e2
      |_ -> failwith "unknown expression";;

let emptyenv () = []

let ext env x v = (x,v) :: env

(*
let rec lookup x env =
  match env with
     | [] -> failwith ("unbound variable: " ^ x)
     | (y,v)::tl -> if x=y then v 
    else lookup x tl 
    *)


print_intval (eval2 (Plus(IntLit 2, IntLit 2)));;
(*
  print_intval (eval2 (Plus(IntLit 1,     BoolLit true)));;
*)
(*
  print_intval (eval2 (Plus(BoolLit true, IntLit 2)));;
*)
(*
  print_intval (eval2 (Plus(BoolLit true, BoolLit true)));;
*)
