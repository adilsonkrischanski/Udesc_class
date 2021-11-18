import math

F = 2428
alfa = math.radians(63)
beta = math.radians(56)


f3 = F / (-(math.tan(alfa))*math.cos(beta) - math.sin(beta))
f1 = f3*(math.cos(beta)/math.cos(alfa))
f2 = -f1*math.cos(alfa)
v2 = -f1*math.sin(alfa)
v3 = -f3*math.sin(beta)

print("F1: ",f1)
print("F2: ",f2)
print("F3: ",f3)
print("H2: ",0)
print("V2: ",v2)
print("V3: ",v3)

