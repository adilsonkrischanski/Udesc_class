# code disponivel em git@github.com:adilsonkrischanski/Udesc_class.git
class graph(): #graph class
    def  __init__(self, nvertices) :
        self.N = nvertices
        self.graph = [[0 for column in range(nvertices)]for row in range(nvertices)]
        self.rotulo = ['0'for column in range(nvertices)]
        

 

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

    def toString(self):
        
        print(f'    ',end="")
        for rot in self.rotulo:
            print(f' {rot} ',end="")
        print("")
        for pos,i in enumerate(self.graph):
            print(f'{self.rotulo[pos]:<3}  {i}')

def sub(sub,principal):
        rotulosSub = sub.rotulo 
        rotulosPrin = principal.rotulo
        grafoP = principal.graph
        grafoS = sub.graph
        verifica = True
        verifica2 = True
        
        for sub in rotulosSub:
            if not (sub in rotulosPrin):
                verifica = False
                break
        
        if verifica:
            for s1 in range(len(rotulosSub)):
                for s2 in range(s1,len(rotulosSub)):
                   
                    p1 = principal.position(rotulosSub[s1])
                    p2 = principal.position(rotulosSub[s2])


                    if not(grafoP[p1][p2] == grafoS[s1][s2]):
                        verifica2 = False
                        break
                        break

            if verifica2:
                print(f"O grafo {sub} é um sub grafo de {principal}")
            else:
                print(f"{sub} Nao é um sub Grafo de {principal}")

        else:
            print("Os Rotulos nao sao correspondentes")


