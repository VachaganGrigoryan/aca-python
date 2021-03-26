class Node:

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f'Node({self.value})'

    def __str__(self):
        return f'{self.value}'


class Graph:

    def __init__(self):
        self.Edge: dict = {}
        self.Vertex: dict = {}
        self.Neighbours: dict = {}

    def add_vertex(self, i):
        if i not in self.Vertex:
            self.Vertex[i] = Node(i)
            self.Neighbours[i] = set()

    def delete_vertex(self, i):
        if i in self.Vertex:
            self.Vertex.pop(i)
            for edge in list(self.Edge.keys()):
                if i in edge:
                    self.Edge.pop(edge)

            for j in self.Neighbours.pop(i):
                self.Neighbours[j].remove(i)

    def add_edge(self, i, j, weight=None):
        self.add_vertex(i)
        self.add_vertex(j)

        self.Edge[(i, j)] = weight

        self.Neighbours[i].add(j)
        self.Neighbours[j].add(i)

    def delete_edge(self, i, j):
        if (i, j) in self.Edge:
            self.Edge.pop((i, j))
            self.Neighbours[i].remove(j)
            self.Neighbours[j].remove(i)

    def split_edge(self, i, j, w):
        if w not in self.Vertex and (i, j) in self.Edge:
            self.delete_edge(i, j)
            self.add_edge(i, w)
            self.add_edge(w, j)

    def subgraph_contraction(self, subgraph):
        if subgraph in self:
            pass

    def graph_supplement(self):
        supplement = Graph()

        for i, neighbours in self.Neighbours.items():
            for j in self.Vertex.keys():
                if i != j and j not in neighbours and (j, i) not in supplement.Edge:
                    supplement.add_edge(i, j)

        return supplement

    def __contains__(self, graph_2):
        if not isinstance(graph_2, Graph):
            raise TypeError(f"'in <class 'Graph'>' requires Graph as left operand, not {type(graph_2)}")

        return all(node in self.Vertex for node in graph_2.Vertex) and all(edge in self.Edge for edge in graph_2.Edge)

    def __str__(self):
        return f'Edge: {self.Edge}, \nVertex: {self.Vertex}, \nNeighbours: {self.Neighbours}'


if __name__ == '__main__':
    # graph_1 = Graph()
    # graph_1.add_edge(1, 2)
    # graph_1.add_edge(1, 3)
    # graph_1.add_edge(2, 3)
    # graph_1.add_edge(1, 5)
    # graph_1.add_edge(2, 6)
    # graph_1.add_edge(3, 4)
    # graph_1.add_edge(4, 5)
    # graph_1.add_edge(4, 6)
    # graph_1.add_edge(5, 6)
    # graph_1.add_edge(5, 7)
    # graph_1.add_edge(6, 7)
    #
    # graph_2 = Graph()
    # graph_2.add_edge(1, 2)
    # graph_2.add_edge(1, 3)
    # graph_2.add_edge(2, 3)

    # graph_1.delete_vertex(1)
    # graph_1.delete_edge(1, 2)
    # graph_1.split_edge(3, 4, 9)

    # print(graph_1)
    # print(graph_2)
    #
    # print(graph_2 in graph_1)
    # print(graph_1 in graph_1)

    graph = Graph()
    graph.add_edge(1, 2)
    graph.add_edge(1, 4)
    graph.add_edge(1, 6)
    graph.add_edge(2, 3)
    graph.add_edge(2, 5)
    graph.add_edge(3, 4)
    graph.add_edge(3, 6)
    graph.add_edge(4, 5)
    graph.add_edge(5, 6)

    print(graph)
    print(graph.graph_supplement())
