import numpy
import util
import networkx as nx
import fc.network_tool as nxt



test_list = ['a', 'b', 'c', 'd', 'e']
m = nxt.MatrixNetwork(test_list)
m.add_edges(['a', 'b', 'c', 'd'])
m.add_edge('d','e')
g = m.get_network()
util.show_nw(g)
# m = [[ 0,  0,  0,  1,  1,  0,  0],
# [ 0,  0,  1,  0,  0,  0,  0],
# [ 0,  1,  0,  0,  0,  0,  0],
# [ 1,  0,  0,  0,  1,  0,  0],
# [ 1,  0,  0,  1,  0,  1,  1],
# [ 0,  0,  0,  0,  1,  0,  1],
# [ 0,  0,  0,  0,  1,  1,  0]]
#
# A = numpy.matrix(m)
# G=nx.from_numpy_matrix(A)
#
# # 修改标签
# mapping={0:'a',1:'b',2:'c'}
# G=nx.relabel_nodes(G,mapping)
# util.show_nw(G)