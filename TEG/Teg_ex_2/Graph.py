from Vertex import Vertex

class Graph(): # class graph
   
    def __init__(self):
        self.vert_dict = {}
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

    def add_edge(self, frm, to, cost = 0): #add a new edge
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):   
        return self.vert_dict.keys()

    def adj(self, rot1, rot2): #check adjacence between rot1 and rot2, rot1 and rot2 are label
        if rot1 in self.vert_dict and rot2 in self.vert_dict:
            vertex = self.get_vertex(rot1)
            if self.get_vertex(rot2) in vertex.adj:
                print(f'{rot1} é adjacente a {rot2} a uma distância de {vertex.get_weight(self.get_vertex(rot2))}')
            else:
                print('Não são adjacentes')
        elif rot1 in self.vert_dict and not(rot2 in self.vert_dict):
            print(f'{rot2} não pertence ao Grafo')
        elif rot2 in self.vert_dict and not(rot1 in self.vert_dict):
            print(f'{rot1} não pertence ao Grafo')
        else:
            print('Os vértices não pertencem ao Grafo')
    
    def edge_count(self): # returns the number of edges
        sum = 0
        for x in self.vert_dict.values():
            sum = sum + len(x.adj)
        return int(sum/2)        

    def complete(self):
        for x in self.vert_dict.values():
            if not(len(self.vert_dict) == (len(x.adj) + 1)):
                return False
        return True

    def grd(self,a): # 'a'  is a label

        for i in self.vert_dict:
            if i==a:
                return(i.grau())
                
        return 0

    
    def toString(self): #error
        for c in self.vert_dict:
            print(c.name()) 