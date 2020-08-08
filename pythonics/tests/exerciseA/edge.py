
class Edge:



    def __init__(self, src: Vertice, dst: Vertice):

        self.src = src

        self.dst = dst



        src.addEdge(self)



    def getDestination(self) -> Vertice:

        return self.dst