lanche = ('hamburguer','suco','pizza','pudim')
#tuplas sao imutaveis


print(lanche[1:])
print(lanche[1:3])
print(lanche[:2])

for c in lanche:
    print(c)

for pos, c in enumerate(lanche): #enumerate serve para pegar a posição tb
    print(c, pos)

print(sorted(lanche)) #mostra em ordem 

a= (2,5,4)
b= (5,8,1,2)
c = a+b #concatena as tuplas

print (c) 

pessoa = ("jose", 19, 'M', 44.13)
