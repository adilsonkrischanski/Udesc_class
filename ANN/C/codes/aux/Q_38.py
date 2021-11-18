Pw = 1000
r = 8.25
Ps = 241.72

pi = 'M_PI'

V = f' (({pi}*x*x)/3.0) * (3*{r}-x)' 

Vs = f'(4/3.0) * ({pi}*{r}*{r}*{r})'

t = f' {Pw}*(({Vs})-({V})) - {Ps}*{Vs}'

print(t)
