import tool.util as util
from matplotlib import pyplot as plt


class show_graph:
    # now the real code :)
    curr_pos = 0

    def __init__(self,filename_list, plots_list, auto_set=False):
        self.filename_list = filename_list
        self.plots_list = plots_list
        self.auto = auto_set
        util.set_ch()

        self.fig = plt.figure()
        self.fig.canvas.mpl_connect('key_press_event', self.key_event)

    def set_range(self,x,y):
        plt.xlim(x[0], x[1])
        plt.ylim(y[0], y[1])
        self.x = x
        self.y = y

    def init_range(self):
        x = self.x
        y = self.y
        plt.xlim(x[0], x[1])
        plt.ylim(y[0], y[1])

    def show(self):
        plt.scatter(self.plots_list[0][0], self.plots_list[0][1])
        plt.title(file_name_list[0])
        plt.show()

    def key_event(self, e):
        if e.key == "right":
            self.curr_pos += 1
        elif e.key == "left":
            self.curr_pos -= 1
        else:
            return
        self.curr_pos %= len(self.plots_list)
        plt.cla()
        if not self.auto:
            self.init_range()
        plt.scatter(self.plots_list[self.curr_pos][0], self.plots_list[self.curr_pos][1])
        plt.title(file_name_list[self.curr_pos])
        print(self.curr_pos)
        self.fig.canvas.draw()


def individual_word(fre_path):
    plots_list = []
    file_list = util.get_file_list(fre_path,".txt")
    for file in file_list:
        rl=util.get_list_from_dicttxt(fre_path+file)
        max_num= len(rl)
        x=list(range(max_num))
        y=rl
        plots_list.append((x,y))
    return file_list, plots_list
    # print(plots_list)


def individual_word_xy(fre_path):
    plots_list = []
    file_list = util.get_file_list(fre_path, ".txt")
    # 删除首个

    for file in file_list:
        xy_list = util.get_list_from_file(fre_path+file)
        del [xy_list[-1]]
        x= []
        y = []
        for xy in xy_list:
            x.append(xy.split("\t")[0])
            y.append(xy.split("\t")[1])
        plots_list.append((x,y))
    return file_list, plots_list
    # print(plots_list)

def accumlate_ratio(fre_path):
    file_name_list = []
    plots_list = []
    file_list = util.get_file_list(fre_path,".txt")
    file_name_list.extend(file_list)
    for file in file_list:
        print(file)
        r = util.get_list_from_file(fre_path+file)
        rl = []
        for ii in r:
            rl.append(float(ii))
            # rl.append(float(ii.split("\t")[1]))
        max_num = len(rl)
        x=list(range(max_num))
        y=rl
        # print(sum(y[0:100]))
        plots_list.append((x,y))
    return file_name_list, plots_list

key_list = util.get_key_list2()
file_name_list, plots_list = individual_word_xy(r"D:\semantic analysis\新结果\去虚词去单字\2017-4-9整理\新连接度分布特性度分布\纠结//")
# file_name_list, plots_list = accumlate_ratio(r"D:\semantic analysis\新结果\去虚词去单字\2017-4-9整理\新连接度分布特性度分布比率斜率//")
# file_name_list, plots_list = accumlate_ratio()
# sg = show_graph(file_name_list, plots_list,True)
sg = show_graph(file_name_list, plots_list, False)

sg.set_range([0,500],[0,200])
sg.show()
