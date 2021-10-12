# code disponivel em git@github.com:adilsonkrischanski/Udesc_class.git
from system import system
from system import menu

s = system()
while True:

    menu()
    op = int(input())

    if op ==0:
        break

    elif op==1:
        s.newGrafo()

    elif op==2: 
        print("Insira o id do grafo que deseja analizar:")
        id = int(input())
        print("os rotulos presentes nesse grafo são:")
        print(s.grafos[id].rotulo)
        print("Escolha dois rotulos para verificar adjacencia [cuidado com o CAPS LOCK]")
        adj = (input(),input())
        a=s.grafos[id].adjc(s.grafos[id],adj[0],adj[1])
        
        if a>0:
            print(f"E adjacente e tem valor {a}")                    
        else:
            print("nao é adjacente")

    elif op==3: #ok
        print("Insira o id do grafo que deseja analizar:")
        id = int(input())
        print("os rotulos presentes nesse grafo são:")
        print(s.grafos[id].get_vertices())
        print("Escolha o rotulo para verificar verificar o grau [cuidado com o CAPS LOCK]")
        grau = input()
        g = s.grafos[id].grd(grau)
        print(f'O grau maximo é {g}')

    elif op==4: 
        print("Insira o id do grafo que deseja analizar:")
        id = int(input())
        arestas =s.grafos[id].conta_arestas()
        print(f" o grafo tem {arestas} arestas")

    elif op==5:
        print("Insira o id do grafo que deseja analizar:")
        id = int(input())
        c = s.grafos[id].complete()
        if c:
            print("O grafo é completo")
        else:
            print('O grafo nao e completo')

    elif op==6:
        print("Insira o ID do grafo  principal:")
        id1 = int(input())
        print("insira o ID do candidato a sub grafo ")
        id2 = int(input())
        verifica = s.sub(id1,id2)
        if verifica:
            print("E sub Grafo")
        else:
            print("Nao e Subgrafo")


    elif op==7:
        s.toString() #error

    else:
        print("Opcao nao cadastrada, tente Novamente")

