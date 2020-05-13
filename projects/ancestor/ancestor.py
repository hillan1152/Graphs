from graph import Graph
from util import Queue

def earliest_ancestor(ancestors, starting_node):
    g = Graph()
    for ancestor in ancestors:
        g.add_vertex(ancestor[0])
        g.add_vertex(ancestor[1])
        g.add_edge(ancestor[1], ancestor[0])
    print(g.dft(starting_node))

        
    # print(g.get_neighbors(8))


    pass

if __name__ == '__main__':
    test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    earliest_ancestor(test_ancestors, 3)