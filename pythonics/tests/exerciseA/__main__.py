try:
	from exerciseA import  edge
except NameError as error:
	print(False)
	import exerciseA.edge as edges
try:	
	from exerciseA import vertice
except NameError as error:
	print(False)	

setattr(edge,"Vertice",Vertice)
print(edge.vertice)