class graph(): #graph class
    def  __init__(self, nvertices) :
        self.N = nvertices
        self.grafh = [[0 for column in range(nvertices)]for row in range(nvertices)]
        self.rotulo = ['0'for column in range(nvertices)]
    
    def complete(self,i,j,w): # insert the value  in position and in transposed position
        self.grafh[i][j] = w
        self.grafh[j][i] = w


    def renameR(self):
        for i in range(self.N):
            self.rotulo[i] = input(f"qual rotulo de {i}:")

    def readWheighrs(self, g):
        for i in range(self.N):
            for j in range(self.N):
                if(i < j):
                    a =int(input(f'Digite o peso entre {self.rotulo[i]} e {self.rotulo[j]}: '))
                    g.complete(i,j,a)

    def position(self,a): #return the position of 'a'
        for pos,rotulo in enumerate(self.rotulo):
            if a == rotulo:
                return pos
        return -1
    
    def adjc(self,g,a,b): #adjacence check 
  
        primary = g.position(a) 
        second = g.position(b) 
        

        if(primary ==-1) or (second ==-1):
            return "Invervalo Invalido"
            
        
        else:
            if(self.grafh[primary][second]!=0):
                return True
            else:
                return False
        
    def grd(self, u ): 
         count =0
         for c in self.grafh[u]:
             if c!=0:
                 count+=1
         return count

    def edge(self): # check how many edges are in the graph  
        count =0
        for c in self.grafh:
            for aresta in c:
                if aresta !=0:
                    count+=1
        return int(count/2) 

    def graph_is_complete(self): # check if the graph is complete
        for i in range(self.N):
            for j in range(self.N):
                if i!=j:
                    if self.grafh[i][j] ==0:
                        return False
        return True





n = int(input("qual o numero  de vertices: "))
grafo = graph(n)


grafo.renameR()
grafo.readWheighrs(grafo)


print(grafo.grafh)
print(grafo.rotulo)
print(grafo.adjc(grafo,'A','B'))
print(grafo.grd(grafo.position('A')))
print(grafo.edge())
print(grafo.graph_is_complete())

