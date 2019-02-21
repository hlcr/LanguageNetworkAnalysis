import numpy
import networkx as nx


class MatrixNetwork:
    def __init__(self, all_words):
        length = len(all_words)
        self.matrix = numpy.zeros([length, length], bool)
        self.w_dict = {}
        i = 0
        while i < length:
            # 生成字典
            self.w_dict[all_words[i]] = i
            i += 1

    # 获取数字对词语的映射
    def get_num2word_dict(self):
        return dict((v,k) for k,v in self.w_dict.items())


    # 添加单边
    def add_edge(self, node1, node2):
        i = self.w_dict[node1]
        j = self.w_dict[node2]
        self.matrix[i][j] = True
        self.matrix[j][i] = True


    # 把集合edges的所有点都连接起来
    def add_edges(self, nodes):
        i = 0
        j = 0
        while i < len(nodes):
            j = i
            while j < len(nodes)-1:
                j += 1
                self.add_edge(nodes[i],nodes[j])
            i += 1

    # 把集合edges的所有点都连接起来
    def add_gram_edges(self, nodes):
        i = 0
        j = 0
        while i < len(nodes):
            j = i
            while j < i+2 and j < len(nodes)-1:
                j += 1
                self.add_edge(nodes[i], nodes[j])
            i += 1
        # self.add_edge(nodes[len(nodes)-3], nodes[len(nodes)-1])


    # 获取生成网络
    def get_network(self):
        g = nx.from_numpy_matrix(self.matrix)
        return nx.relabel_nodes(g, self.get_num2word_dict())

if __name__ == '__main__':
    # word_set = []
    # for i in range(10):
    #     word_set.append(str(i))
    # print(word_set)
    # mm = MatrixNetwork(word_set)
    # mm.add_gram_edges(word_set)
    import tool.util as util
    mm = util.get_nw(r"D:\semantic analysis\结果\测试网络\美好\p//2009-09-22.pkl")
    util.show_nw(mm)


