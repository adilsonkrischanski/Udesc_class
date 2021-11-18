g= 9.81
desloc = 4.09
tempo = 1.25

ex = f' - {desloc} - ({g}/(2*x*x))*(sinh(x*{tempo})-sin(x*{tempo}))'
print(ex)