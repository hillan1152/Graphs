from graph import Graph
from util import Queue

def earliest_ancestor(ancestors, starting_node):
    # instantiate graph
    g = Graph()

    # create list that will contain all arrays that = max_len
    longest_lists = []


    # iterate through entire ancestors list
    # Each list is a tuple (parent, child)
    # Assign Vertexes based on this
    for ancestor in ancestors:
        parent = ancestor[0]
        child = ancestor[1]
        g.add_vertex(parent)
        g.add_vertex(child)
        # reverse edge connections to find len of starting node -> completion
        g.add_edge(child, parent)

    # adjusted dfs, created a master list of all links between starting node, returns a "master list"
    all_lists = g.dfs(starting_node)

    # length of lists is 0 == has no parents 
    if len(all_lists) == 0:
        return -1
    
    # finds the maximun length of an item in the list
    max_len = max(len(x) for x in all_lists)

    # if an item in the list == maxList, add to list
    for i in range(0, len(all_lists)):
        curr_list = all_lists[i]
        if len(curr_list) == max_len:
            longest_lists.append(curr_list)
    
    # if more than 1 list contains max_len, find num w/ lowest num and return last number in list
    if len(longest_lists) > 1:
        lowest_num = longest_lists[0][-1]
        for lists in longest_lists:
            if lists[-1] < lowest_num:
                lowest_num = lists[-1]
                return lowest_num    

    # if len is 1, return last number in list
    return longest_lists[0][-1]

    
if __name__ == '__main__':
    test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (4, 5), (4, 8), (8, 9), (10, 1), (14, 4)]
    earliest_ancestor(test_ancestors, 6)