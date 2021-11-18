import threading, queue
class graph(): #graph class
    def  __init__(self, nvertices) :
        self.N = nvertices
        self.graph = [[0 for column in range(nvertices)]for row in range(nvertices)]
        self.rotulo = ['0'for column in range(nvertices)]
        self.ListExplored = []
        

 

    def complete(self,i,j,w): # insert the value  in position and in transposed position
        self.graph[i][j] = w
        self.graph[j][i] = w


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
  
        first = g.position(a) 
        second = g.position(b) 
        

        if(first ==-1) or (second ==-1):
            return "Invervalo Invalido"
            
        
        else:
            if(self.graph[first][second]!=0): 
                return self.graph[first][second]
            else:
                return 0
        
    def grd(self, u ): 
         count =0
         for c in self.graph[u]:
             if c!=0:
                 count+=1
         return count

    def edge(self): # check how many edges are in the graph  
        count =0
        for c in self.graph:
            for aresta in c:
                if aresta !=0:
                    count+=1
        return int(count/2) 

    def graph_is_complete(self): # check if the graph is complete
        for i in range(self.N):
            for j in range(self.N):
                if i!=j:
                    if self.graph[i][j] ==0:
                        return False
        return True

def setAllUnexplored(G):
    G.ListExplored = []


def dfs(G, s): # 'G' is a graph(), 's' is a label
    setAllUnexplored(G);

    stack = []; #creat stack - stack is initialized as an empty list
    stack.append(s);

    while(len(stack) != 0):
        v = stack.pop();
        if not(v in G.ListExplored):
            G.ListExplored.append(v)
        #print(f'{v} explored!') #only test
        for w in range(0, G.N):
            if G.graph[G.position(v)][w] != 0:
                if not(G.rotulo[w] in G.ListExplored):
                    stack.append(G.rotulo[w]) #insert a vertex at position [w] in the final stack
    
    print(G.ListExplored)


if __name__ == '__main__':
   
    meuGrafo = graph(15)

    meuGrafo.rotulo = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14']
    meuGrafo.graph = [
        [0,281,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [281,0,38,238,0,0,0,0,0,0,0,0,0,0,0],
        [0,38,0,0,0,68,0,0,0,0,0,0,0,0,0],
        [0,238,0,0,152,0,74,0,0,0,0,0,0,0,0],
        [0,0,0,152,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,68,0,0,0,271,74,0,0,0,0,0,0,0],
        [0,0,0,74,0,271,0,0,69,0,0,0,0,0,0],
        [0,0,0,0,0,74,0,0,0,70,71,0,0,0,0],
        [0,0,0,0,0,0,69,0,0,206,0,0,0,0,77],
        [0,0,0,0,0,0,0,70,206,0,0,71,0,0,0],
        [0,0,0,0,0,0,0,71,0,0,0,68,0,0,0],
        [0,0,0,0,0,0,0,0,0,71,68,0,74,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,74,0,74,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,74,0,71],
        [0,0,0,0,0,0,0,0,77,0,0,0,0,74,0],
    ]
    dfs(meuGrafo, '7')
