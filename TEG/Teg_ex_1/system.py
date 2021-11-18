# code disponivel em git@github.com:adilsonkrischanski/Udesc_class.git
from graph import *

class system:
    def __init__(self):
        self.grafos = []

    def newGrafo(self):
        n = int(input("qual o numero  de vertices: "))
        grafo = graph(n)
        grafo.renameR()
        grafo.readWheighrs(grafo)
        self.grafos.append(grafo)
        grafo.toString()

    
    def sub(self,principal,sub):
        rotulosSub = self.grafos[sub].rotulo 
        rotulosPrin = self.grafos[principal].rotulo
        grafoP = self.grafos[principal].graph
        grafoS = self.grafos[sub].graph
        verifica = True
        verifica2 = True
        
        for sub in rotulosSub:
            if not (sub in rotulosPrin):
                verifica = False
                break
        
        if verifica:
            for s1 in range(len(rotulosSub)):
                for s2 in range(s1,len(rotulosSub)):
                   
                    p1 = self.grafos[principal].position(rotulosSub[s1])
                    p2 = self.grafos[principal].position(rotulosSub[s2])

                    #print(f"posicao analizada principal {p1}{p2} sub {s1}{s2}")

                    if not(grafoP[p1][p2] == grafoS[s1][s2]):
                        verifica2 = False
                        break
                        break

            if verifica2:
                print("O grafo é um sub grafo")
            else:
                print("Nao é um sub Grafo")

        else:
            print("Os Rotulos nao sao correspondentes")

    def toString(self):
        for pos,grafo in enumerate(self.grafos):
            print("")
            print(f'ID {pos}')
            grafo.toString()
            print("")

    def alcanca(self,id, vertice):
        




def menu():
    print(f"----------------menu---------------")
    print("1 - inserir um novo Grafo")
    print("2 - Verificar Adjacencia ")
    print("3 - verificar Grau")
    print("4 - contar arestas de um grafo")
    print("5 - Verificar se um grafo é completo")
    print("6 - verificar se um um grafo é sub grafo de outro")
    print("7 - Mostar Grafos")
    print("0 - Sair ")
    print("")
