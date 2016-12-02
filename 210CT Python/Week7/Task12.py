

Graph = {
    'A': set(['B', 'C']), 
    'B': set(['A', 'D', 'E']),
    'C': set(['A', 'F']), 
    'D': set(['B', 'G']), 
    'E': set(['B', 'F', 'G']), 
    'F': set(['C', 'E']), 
    'G': set(['E', 'D'])}


class node:
    def __init__(self, node, edges = []):
        self.label = node 
        self.edges = edges


    def __str__(self):
        return 'Node(' + str(self.label) + ", " + str(self.edges) +")"


class Graph(node): 
    def __init__(self):
        self.nodes = {}


    def addnode(self,name): 
        self.node[name] = node(name)

    def addedge(self, source, target):
        self.nodes[source].edges = self.node[source].edges + [target]

    def dot(self):
        for nodename in self.node:
            for edge in self.node[nodename].edges: 
                print(str(nodename) + " -> "+ str(edge))

if __name__ == '__main__':
    G = Graph() 
    G.addnode(A) 
    G.addedge(A) 
    G.addnode(B,C) 
    G.addnode(D) 
    G.addedge(B,C) 
    G.addnode(E) 
    G.addedge(E,F) 
    G.addnode(G) 
    G.addedge(G,D)
