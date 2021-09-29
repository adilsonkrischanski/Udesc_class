from random import randrange
a = (randrange(1,10),randrange(1,10),randrange(1,10),randrange(1,10),randrange(1,10)) #randomizador
print(a)
print(f'O maior numero é {sorted(a)[-1]} e o menor é {sorted(a)[0]}')