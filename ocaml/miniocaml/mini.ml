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
  | IntVal of int
  | BoolVal of bool

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
      begin
        match (eval2 e1,eval2 e2) with
          |(IntVal(n1), IntVal(n2)) -> IntVal(n1+n2)
          |_ -> failwith "integer values expected"
      end
    |Times(e1, e2) -> 
        begin
          match (eval2 e1, eval2 e2) with
            |(IntVal(n1), IntVal(n2)) -> IntVal(n1*n2)
            |_ -> failwith "integer values expected"
        end
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
    |_ -> failwith "unknown expression";;

let print_intval value = match value with
    |IntVal(i) -> print_int i 
    |BoolVal(true) -> print_int 1
    |BoolVal(false) -> print_int 0;;

print_intval (eval2 (Plus(IntLit 1,     IntLit 2)));;
(*
  print_intval (eval2 (Plus(IntLit 1,     BoolLit true)));;
*)
(*
  print_intval (eval2 (Plus(BoolLit true, IntLit 2)));;
*)
(*
  print_intval (eval2 (Plus(BoolLit true, BoolLit true)));;
*)
