posNeg n = rem (n-1) 4 == 0

baixo 1 = [1]
baixo x
  | rem x 2 == 0 = baixo (x-1)
  | posNeg x = (x) : baixo (x-2)
  | otherwise = -(x) : baixo (x-2)

head' [] = 1
head' (x:xs) = x


chamaPI 1 = 4.0
chamaPI n = 4 / head' (baixo n) + chamaPI n-2

chamaPI' 1 a = a
chamaPI' n ac = chamaPI' (n-2) (ac+(4 / head' (baixo n)))


1000*(((4/3)*pi*5.95^3)-(((pi*x^2))/3)*(3*5.95-x)))-( 709.92 * ((4/3)*pi*5.95^3));

