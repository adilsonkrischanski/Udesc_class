import sys

class Vertex():
    
    def __init__(self, id):
        self.id = id
        self.adj = {}
        self.explored = 0

    def name(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adj])

    def add_neighbor(self, neighbor, weight=0):
        self.adj[neighbor] = weight

    def get_connections(self):
        return self.adj.keys()  

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adj[neighbor]

    def grau(self):
        return len(self.adj)

class Graph(): 
   
    def __init__(self):
        self.vert_dict = dict()
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

    def adj(self, vA, vB):
        #verifica se A e B pertencem ao grafo 
        if vA in self.vert_dict and vB in self.vert_dict:
            vertex = self.get_vertex(vA)
            #verifica se vB está na lista de adj de A
            if self.get_vertex(vB) in vertex.adj:
                print(f'{vA} é adjacente a {vB} a uma distância de {vertex.get_weight(self.get_vertex(vB))}')
                return True;
            else:
                print('Não são adjacentes')
        #exceção 1
        elif vA in self.vert_dict and not(vB in self.vert_dict):
            print(f'{vB} não pertence ao Grafo')
        #exceção 2
        elif vB in self.vert_dict and not(vA in self.vert_dict):
            print(f'{vA} não pertence ao Grafo')
        #exceção 3
        else:
            print('Os vértices não pertencem ao Grafo')
    
    def conta_arestas(self):
        sum = 0
        #conta todas as arestas e divide por dois para cancelar as repetições
        #Não leva em consideração caminhos paralelos
        for x in self.vert_dict.values():
            sum = sum + len(x.adj)
        return int(sum/2)        

    def complete(self):
        #verifica se cada vértice do grafo é adjacente a todo mundo, exceto a si mesmo
        #Não leva em consideração caminhos paralelos
        for x in self.vert_dict.values():
            if not(len(self.vert_dict) == (len(x.adj) + 1)):
                return False
        return True

def menor_inexplorado(G, d):
    min = sys.maxsize

    for i in d.keys():
        if (G.vert_dict[i].explored == 0):
            print(i)
            print('ok')
        if d[i] < min:
            print('ok2')
            min = d[i]
            rot = i

    return rot

def djikstra(G, s):
    d = dict()
    p = dict()
    for v in G.vert_dict.keys():
        G.vert_dict[v].explored = 0
        d[v] = sys.maxsize
        p[v] = -1

    d[s] = 0
    explorados = []

    while len(explorados) != len(G.vert_dict):
        u = menor_inexplorado(G, d)
        explorados.append(u)
        G.vert_dict[u].explored = 1

        for w in G.vert_dict[u].get_connections():
            if w.explored == 0 and d[u] + G.vert_dict[u].get_weight(w) < d[w.id]:
                d[w] = G.vert_dict[u].get_weight(w)
                p[w] = u

    print(d)
    print('\n')
    print(p)


if __name__ == '__main__':

    #Meu grafo setado
    g = Graph()
    g.vert_dict = {'A': Vertex('A'),
                   'B': Vertex('B'),
                   'C': Vertex('C'),
                   'D': Vertex('D'),
                   'E': Vertex('E'),
                   'F': Vertex('F'),
                   'G': Vertex('G'),
                   'H': Vertex('H'),
                   'I': Vertex('I'),
                   'J': Vertex('J'),
                   'K': Vertex('K'),
                   'L': Vertex('L'),
                   'M': Vertex('M')}

    g.add_edge('A','B', 52)
    g.add_edge('B','A', 52)
    g.add_edge('B','C', 163)
    g.add_edge('B','E', 57)
    g.add_edge('C','B', 163)
    g.add_edge('C','D', 57)
    g.add_edge('D','E', 164)
    g.add_edge('D','C', 57)
    g.add_edge('E','D', 164)
    g.add_edge('E','B', 57)
    g.add_edge('E','F', 56)
    g.add_edge('F','G', 53)
    g.add_edge('F','E', 56)
    g.add_edge('F','M', 160)
    g.add_edge('G','F', 53)
    g.add_edge('G','L', 161)
    g.add_edge('G','H', 53)
    g.add_edge('H','G', 53)
    g.add_edge('H','K', 160)
    g.add_edge('H','I', 56)
    g.add_edge('I','H', 56)
    g.add_edge('I','J', 160)
    g.add_edge('J','K', 57)
    g.add_edge('J','I', 160)
    g.add_edge('K','J', 57)
    g.add_edge('K','H', 160)
    g.add_edge('K','L', 52)
    g.add_edge('L','K', 52)
    g.add_edge('L','G', 161)
    g.add_edge('L','M', 55)
    g.add_edge('M','L', 55)
    g.add_edge('M','F', 160)


    djikstra(g, 'H')
