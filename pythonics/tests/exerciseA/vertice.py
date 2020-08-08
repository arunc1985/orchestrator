
class Vertice:



    def __init__(self, key: str):

        self.key = key

        self.edges = list()



    def getKey(self) -> str:

        return self.key



    def addEdge(self, edge: Edge):

        self.edges.append(edge)



    def addEdges(self, edges: List[Edge]):

        self.edges.extend(edges)



    def getEdge(self, dst: str) -> Edge:

        for edge in self.edges:

            if edge.dst == dst:

                return edge

        return None



    def getAllEdges(self) -> List[Edge]:

        return self.edges



    def isPathExists(self, dst: str) -> bool:

        return False if not self.getEdge(dst) else True


