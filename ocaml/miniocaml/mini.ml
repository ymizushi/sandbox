type exp = IntLit of int
| Plus of exp * exp
| Minus of exp * exp
| Div  of exp * exp
| Mul  of exp * exp
| Times of exp * exp;;

let rec eval1 e = 
  match e with
  |IntLit(n) -> n
  |Plus(e1, e2) -> (eval e1) + (eval e2)
  |Times(e1, e2) -> (eval e1) * (eval1 e2)

(IntLit 2)
