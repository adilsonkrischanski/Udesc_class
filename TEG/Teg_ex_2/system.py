from Graph import Graph
class system:

    def __init__(self):
        self.grafos = []

    def newGrafo(self):
        grafo = Graph()
        vert = int(input("Deseja inserir quantos Vetcices?"))
        for c in range(0,vert):
            rot = input("Qual o rotulo desejado: ")
            grafo.add_vertex(rot)
        arestas = int(input("quantas arestas deseja Inserir: "))
        for i in range(0,arestas):
            a = (input("insira o rotulo de saida: "),input("Insira o rotulo de destino"),int(input("Insira o peso da aresta: ")))
            grafo.add_edge(a[0],a[1],a[2])
        grafo.toString()


    def toString(self):
        for pos,grafo in enumerate(self.grafos):
            print("")
            print(f'ID {pos}')
            grafo.toString() #error
            print("")


    def subgraph(self, subid, principalid): # check is subgraph, subid and principalid are Graphs
        sub = self.grafos[subid]
        principal = self.grafos[principalid]
        verifica = True
        for x in sub.vert_dict.keys():
            if x in principal.vert_dict.keys():
                verifica = verifica and True
            else:
                verifica = verifica and False
            
        if verifica:
            for i in sub.vert_dict.values():
                for j in principal.vert_dict.values():
                    if i.id == j.id:
                        for x in i.adj.keys():
                            for w in j.adj.keys():
                                if x.id == w.id:
                                    if i.adj[x] == j.adj[w]:
                                        verifica = verifica and True
                                    else:
                                        verifica = verifica and False
                                    break;

            if verifica:
                return True
            else:
               return False

        else:
            return False
 


def menu():
    print(f"----------------menu---------------")
    print("1 - inserir um novo Grafo")
    print("2 - Verificar Adjacencia ")
    print("3 - verificar Grau")
    print("4 - contar arestas de um grafo")
    print("5 - Verificar se um grafo é completo")
    print("6 - verificar se um um grafo é sub grafo de outro")
    print("7 - Mostar Grafos") #error
    print("0 - Sair ")
    print("")