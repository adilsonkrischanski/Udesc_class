seq = [1,2,3,5,1] #lista de sequencia para teste

def ciclo(sequencia): #função que verifica ciclo
    verifica = True
    if sequencia[0] == sequencia[len(sequencia)-1]:
        for c in range(1,len(sequencia)-1):
            for i in range(c+1,len(sequencia)-1):
                if sequencia[c]==sequencia[i]:
                    verifica = False
                    break

    if verifica:
        return True
    else:
        return False

print(ciclo(seq)) #mosta a resposta no consoles