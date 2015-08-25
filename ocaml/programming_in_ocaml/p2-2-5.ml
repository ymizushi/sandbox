(* 2.1.1. Syntax Error *)

(* 2.1.2 *)
print_int (-2+3);;
print_char '\n';;

(* 2.1.3 *)
print_int (9/ -4);; (* / と - をひっつけるとエラー*)
print_char '\n';;

(* 2.1.4 *)
print_int (+3 + 5);;
print_char '\n';;

(* 2.2.1 *)
print_float (float_of_int 3 +. 2.5);; 
print_char '\n';;

(* 2.2.2 *)
print_int (int_of_float 0.7);; 
print_char '\n';;

(* 2.2.3 *)
print_int ((int_of_char 'A') + 20);; 
print_char '\n';;

(* 2.2.4 *)
print_int (int_of_string "0xff");; 
print_char '\n';;

(* 2.2.5 *)
print_float (5.0 ** 2.0);; 
print_char '\n';;

(* 2.3.1 *)
(* 8*-2
 * 誤っている点: *と-にスペースがない
 *)
print_int (8* -2);; 
print_char '\n';;

(* 2.3.2 *)
(* int_of_string "0xfg"
 * 誤っている点: 引数のstring型はint型に変換出来る値ではない
 *)
print_int (int_of_string "0xff");;
print_char '\n';;

(* 2.3.3 *)
(* int_of_float -0.7
 * 誤っている点: int_of_float - 0.7 と判断してしまうから
 *)
print_int (int_of_float (-0.7));;
print_char '\n';;

(* 2.4.1 *)
print_float (float_of_int (int_of_float 5.0));;
print_char '\n';;

(* 2.4.2 ? *)
print_float (sin (3.14 /. 2.0) ** 2.0 +. cos (3.14 /. 2.0) ** 2.0);;
print_char '\n';;

(* 2.4.3 *)
print_float (sqrt (float_of_int (3 * 3 + 4 * 4)));;
print_char '\n';;
