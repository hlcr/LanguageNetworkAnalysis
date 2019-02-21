import util


def la():
    kl = ['吐槽', '淡定', '自拍']
    for key in kl:
        rl = []
        srl = []
        wl = util.get_list_from_file('D:\文档\项目\数据采集文档\词频分布//' + key +'.txt')
        for w in wl:
            wwl = w.split('\t')
            if len(wwl[0]) > 1 and int(wwl[1]) > 10:
                rl.append({'word':wwl[0],'num':int(wwl[1])})
        rl.sort(key=lambda obj: obj.get('num'), reverse=True)
        for rrl in rl:
            srl.append(rrl['word']+'\t'+str(rrl['num']))
        util.save_file('D:\文档\项目\数据采集文档\词频分布//' + key +'r.txt',srl)


def lb():
    rr_dict ={}
    rr_set = set()
    kl = util.get_key_list()
    for key in kl:
        print(key)
        wl = util.get_list_from_file('D:\文档\项目\数据采集文档\词频分布//r//' + key +'r.txt')
        i = 0
        r_set = set()
        while i < 8000 and i < len(wl):
            wwl = wl[i].split('\t')
            num = rr_dict.get(wwl[0])
            r_set.add(wwl[0])
            if num is None:
                rr_dict[wwl[0]] = wwl[1]
            else:
                rr_dict[wwl[0]] = int(num) + int(wwl[1])
            i += 1
        if len(rr_set) == 0:
            rr_set = rr_set | r_set
        else:
            rr_set = rr_set & r_set

    kl_list = []
    srl = []
    for ww in rr_set:
        num = rr_dict.get(ww)
        kl_list.append({'word': ww, 'num': num})
    kl_list.sort(key=lambda obj: obj.get('num'), reverse=True)
    for rrl in kl_list:
        srl.append(rrl['word'] + '\t' + str(rrl['num']))
    util.save_file('D:\文档\项目\数据采集文档\词频分布//' + 'result' + 'r.txt', srl)


lb()

