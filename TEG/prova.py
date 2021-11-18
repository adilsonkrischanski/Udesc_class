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


def prova_q3(G, e, s): # 'G' é um grafo, 'e' é  vertice de entrada no labirinto, 's' é o grafo de saida do labirinto
    #metodo baseado em busca em profundidade
    setAllUnexplored(G); # limpamos o parametro de vertices explorados 

    stack = []; #criamos uma lista vazia / ela sera utilizada como pilha
    stack.append(e); # colocamos o vertice de entrada na pilha 

    while(len(stack) != 0): #enquanto nossa pilha não estiver vazia 
        v = stack.pop(); #o comando pop, retorma o ultimo vertex colocado na pilha e o remove da pilha, colocamos esse valor na variavel v
        if not(v in G.ListExplored): #se v não estiver na lista de explorado 
            G.ListExplored.append(v) # sendo verdade o if da linha anterior então colocamos v na lista e explorados
            print(v)
        if v==s: #verificamos se o vertice v é o vertice de saida 
            print("o Caminho foi concluido com sucesso") # pritamos q chegamos no vertice de saida e
            print(G.ListExplored) #printamos a lista de explorados 
            return 1 ; #como encontramos oq queriamos damos um return 1 para informar q o caminho foi encontrado com sucesso e o labirinto possui uma saida
        else: #caso v não seja o vertice desejado 
            for w in range(0, G.N): #fazemos um for perforrendo todos os vertices de G
                print(f'{G.position(v)},{w}')
                if G.graph[G.position(v)][w] != 0: #verifivamos se se no grafo G na posição de Relaciona os vertices 
                    if not(G.rotulo[w] in G.ListExplored): #se o vertice anterior ainda não tiver incluso da lista de rotulos explorados
                        stack.append(G.rotulo[w]) #então inserimos o vertice v na lista pilha para ser explorado a diante.
    
    #print(G.ListExplored) 
   
    print("o grafo n tem saida") #caso em nenhum momento ele encontre o grafo de saida na linha  88 entaão ele chegara aqui e dira q o labririnto não tem saida
    print(G.ListExplored) #printamos a lista de explorados
    print(v) 
    return 0 # retorna 0 representando a falha de o grafo n tem saida.



if __name__ == '__main__':
   
    meuGrafo = graph(22)

    meuGrafo.rotulo = ['E','0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','16b','17','18','S']
    meuGrafo.graph = [
        [0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
        [0,0,0,1,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,1],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0]]
    
    prova_q3(meuGrafo, 'E' , 'S') 
