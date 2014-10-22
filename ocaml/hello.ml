let rec quicksort = function
  | [] -> []
  | pivot :: rest ->
      let is_less x = x < pivot in
      let left, right = List.partition is_less rest in
      quicksort left @ [pivot] @ quicksort right
