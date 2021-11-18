L = 4.25
r = 3.19
V = 34.04
pi ='M_PI'

E = f'-{V} +{L}*(0.5*{pi}*{r}*{r} - {r}*{r}*asin(x/{r}) - x*sqrt({r}*{r}-x*x))'

print(E)