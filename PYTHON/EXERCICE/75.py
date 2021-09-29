t = (int(input()),int(input()),int(input()),int(input()))

contnove =0
pos3= []
pares =[]

for pos, c in enumerate(t):
    #repeticao do numero 9
    if c==9:
        contnove+=1
    #valores pares 
    if c%2 == 0:
        pares.append(c)
    if c==3:
        pos3.append(pos)
    

print(f'O valor 9 apareceu {contnove} vezes')
if(pos3 != []):
    print(f'o valor 3 aparece na posicao {pos3}')
else:
    print('o valor 3 nao aparece na tupla')
print(f'os numeros pares sao {pares}')