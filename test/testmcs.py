# def testmcs():
#     g1 = nx.Graph()
#     # g1.add_edge('a', 'b')
#     g1.add_edge('b', 'c')
#     g1.add_edge('h', 'a')
#     g1.add_edge('i', 'a')
#     g1.add_edge('i', 'h')
#     g1.add_edge('i', 't')
#     g1.add_edge('i', 'j')
#     g1.add_edge('t','j')
#
#
#     g2 = nx.Graph()
#     g2.add_edge('b', 'd')
#     g2.add_edge('d','e')
#     g2.add_edge('d','a')
#     g2.add_edge('h', 'a')
#     g2.add_edge('h', 'i')
#     g2.add_edge('i', 'a')
#     g2.add_edge('i', 'k')
#     g2.add_edge('i', 'j')
#     g2.add_edge('h', 'j')
#
#     g3 = mcs(g1,g2)
#     print(mcs_ratio(g3, g2, 'a'))
#     nodelist = ['a', 'b', 'c', 'h', 'i', 'j', 't']
#     print(nx.to_numpy_matrix(g1, nodelist))
#     print(nodelist)
#     util.show_nw(g1)
