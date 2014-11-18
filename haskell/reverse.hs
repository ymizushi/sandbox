rev ::  String -> String -> String
rev input output
  |input == "" = output
  |otherwise =  
    let c = head input in 
    let rest = tail input in 
        (rev rest ([c] ++ output))

rever :: String -> String -> String
rever "" output = output
rever input output = 
  let c = head input in 
  let rest = tail input in 
  (rever rest ([c] ++ output))
    

main = 
  print (rever "piyo" "")
