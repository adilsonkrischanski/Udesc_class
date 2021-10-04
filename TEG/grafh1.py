class grafh():
    def  __init__(self, nvertices) :
        self.N = nvertices
        self.grafh = [[0 for column in range(nvertices)]for row in range(nvertices)]
        self.V = ['0'for column in range(nvertices)]
        
    def mudaNome(self):
        for i in range(self.N):
            self.V[i] = input(f"qual rotulo de {i}:")

    def readWheighrs(self):
        for i in range(self.N):
            for j in range(self.N):
                if(i!=j):
                    self.grafh[i][j] = int(input(f'Digite o peso entre {self.V[i]} e {self.V[i]}'))


n = int(input("qual o numero  de vertices: "))
grafo = grafh(n)


grafo.mudaNome()
grafo.readWheighrs()

print(grafo.grafh)
print(grafo.V)