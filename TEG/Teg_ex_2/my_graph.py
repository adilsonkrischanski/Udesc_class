# code disponivel em git@github.com:adilsonkrischanski/Udesc_class.git
from Graph import Graph

g = Graph()

g.add_vertex('0')
g.add_vertex('1')
g.add_vertex('2')
g.add_vertex('3')
g.add_vertex('4')
g.add_vertex('5')
g.add_vertex('6')
g.add_vertex('7')
g.add_vertex('8')
g.add_vertex('9')
g.add_vertex('10')
g.add_vertex('11')
g.add_vertex('12')
g.add_vertex('13')
g.add_vertex('14')

g.add_edge('0' , '1', 281) 
g.add_edge('1' , '0', 281) 
g.add_edge('1' , '2',  38) 
g.add_edge('2' , '1',  38) 
g.add_edge('1' , '3', 238) 
g.add_edge('3' , '1', 238) 
g.add_edge('3' , '4', 152) 
g.add_edge('4' , '3', 152)
g.add_edge('2' , '5',  62) 
g.add_edge('5' , '2',  62)
g.add_edge('6' , '3',  74) 
g.add_edge('3' , '6',  74)
g.add_edge('5' , '6', 271) 
g.add_edge('6' , '5', 271)
g.add_edge('5' , '7',  74) 
g.add_edge('7' , '5',  74)
g.add_edge('6' , '8',  69) 
g.add_edge('8' , '6',  69)
g.add_edge('7' , '9',  70) 
g.add_edge('9' , '7',  70)
g.add_edge('7' , '10', 71)
g.add_edge('10', '7',  71)
g.add_edge('10', '11', 68)
g.add_edge('11', '10', 68)
g.add_edge('9' , '11', 71)
g.add_edge('11', '9',  71)
g.add_edge('9' , '8', 206)
g.add_edge('8' , '9', 206)
g.add_edge('11', '12', 74)
g.add_edge('12', '11', 74)
g.add_edge('12', '13', 74)
g.add_edge('13', '12', 74)
g.add_edge('13', '14', 71)
g.add_edge('14', '13', 71)
g.add_edge('14', '8',  77)
g.add_edge('8' , '14', 77)





