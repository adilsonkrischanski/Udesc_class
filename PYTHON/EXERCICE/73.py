vencedores = ('Joao', 'Maria', 'Jose','Lucas','Fernando','Lula','Bolsonaro','Baldo','Jonas','Francico')

#os 5 primeiros
print(vencedores[:6])
#os 4 ultimos
print(vencedores[-4:])
#em ordem alfabetica
print(sorted(vencedores))
#em que posição esta lula
print(f'lula esta na posicao {vencedores.index("Lula")+1}')
