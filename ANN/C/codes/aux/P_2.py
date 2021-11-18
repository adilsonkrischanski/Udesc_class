lambida = 1.41 * pow(10,-10)
n = 127288399
infectados = n*(1/4)

f = f'({n}+1)/(1+{n}*pow(M_E,-{lambida}*({n}+1)*x)) - {infectados}'

print(f)