# 用于抽样采集大范围的数据
import random
import os
from urllib import parse
import tool.util as util

def create_url_word(sword):
    string = parse.quote(sword)
    strArray = string.split('%')
    rword = ''
    for i in range(1,len(strArray)):
        rword += ('%25'+strArray[i])
    return rword


def create_inital_address(word, m_year, m_month):
    year = 2010
    month = 1
    urlList = []
    dateList = []
    # 转折点前的页数收集规则，一月采集三天，一天采集两次
    while year != m_year or month != m_month:
        i = 1
        while i < 4:
            day = random.randint(1+10*(i-1), 10*i)
            i = i + 1
            date = str(year) + '-' + str(month).zfill(2) + '-' + str(day).zfill(2)
            print(date)
            url = 'http://s.weibo.com/weibo/'+word+'&scope=ori&suball=1&timescope=custom:'+date+'-15:'+date+'-23&Refer=g'
            urlList.append(url)
            url = 'http://s.weibo.com/weibo/'+word+'&scope=ori&suball=1&timescope=custom:'+date+'-0:'+date+'-14&Refer=g'
            urlList.append(url)
            dateList.append(date)
        month += 1;
        if month == 13:
            month = 1
            year += 1


    while year != 2015 or month != 12:
        i = 1
        while i < 4:
            day = random.randint(1+10*(i-1), 10*i)
            i += 1
            # 根据日期规则 构造日期
            date = str(year) + '-' + str(month).zfill(2) + '-' + str(day).zfill(2)
            dateList.append(date)
            for k in range(8, 24, 2):
                url = 'http://s.weibo.com/weibo/'+word+'&scope=ori&suball=1&timescope=custom:'+date+'-'+str(k)+':'+date+'-'+str(k+1)+'&page=1'
                urlList.append(url)
            for k in range(0, 2, 1):
                url = 'http://s.weibo.com/weibo/'+word+'&scope=ori&suball=1&timescope=custom:'+date+'-'+str(k)+':'+date+'-'+str(k)+'&page=1'
                urlList.append(url)
            url = 'http://s.weibo.com/weibo/'+word+'&scope=ori&suball=1&timescope=custom:'+date+'-2'+':'+date+'-4'+'&page=1'
            urlList.append(url)
            url = 'http://s.weibo.com/weibo/'+word+'&scope=ori&suball=1&timescope=custom:'+date+'-5'+':'+date+'-7'+'&page=1'
            urlList.append(url)
        month += 1;
        if month == 13:
            month = 1
            year += 1

    return urlList,dateList


def create_inital_address1(word):
    year = 2010
    month = 1
    urlList = []
    dateList = []
    i = 1
    while year < 2016:
        month = 1
        while month < 13:
            i = 1
            while i < 4:
                day = random.randint(1+10*(i-1), 10*i)
                i = i + 1
                date = str(year) + '-' + str(month).zfill(2) + '-' + str(day).zfill(2)
                url = 'http://s.weibo.com/weibo/'+word+'&scope=ori&suball=1&timescope=custom:'+date+'-15:'+date+'-23&Refer=g'
                urlList.append(url)
                url = 'http://s.weibo.com/weibo/'+word+'&scope=ori&suball=1&timescope=custom:'+date+'-0:'+date+'-14&Refer=g'
                urlList.append(url)
                dateList.append(date)
            month = month + 1;
        year = year + 1;
    return urlList,dateList


# 给定起始日期抓取每小时的数据
def create_inital_address2(word, year, month):
    urlList = []
    dateList = []
    while year != 2016 or month != 1:
        i = 1
        while i < 4:
            day = random.randint(1+10*(i-1), 10*i)
            if month == 2 and day > 28:
                day = 28
            i += 1
            # 根据日期规则 构造日期
            date = str(year) + '-' + str(month).zfill(2) + '-' + str(day).zfill(2)
            dateList.append(date)
            for k in range(0, 24, 1):
                url = 'http://s.weibo.com/weibo/'+word+'&scope=ori&suball=1&timescope=custom:'+date+'-'+str(k)+':'+date+'-'+str(k)
                urlList.append(url)
        month += 1
        if month == 13:
            month = 1
            year += 1
    return urlList,dateList


# 给定日期列表抓取每小时的数据
def create_inital_address3(word, dateList):
    word = util.create_url_word(word)
    urlList = []
    for date in dateList:
        for k in range(0, 24, 1):
            url = 'http://s.weibo.com/weibo/'+word+'&scope=ori&suball=1&timescope=custom:'+date+'-'+str(k)+':'+date+'-'+str(k)
            urlList.append(url)
    return urlList,dateList

def main1():
    sword_list = ["简单","希望","喜欢","无聊","害怕","美好","努力","感觉","气质"]
    for sword in sword_list:
        os.chdir(r'D:\semantic analysis\采集路线\2017-1-9//')
        print('start')
        word = create_url_word(sword)
        print(word)
        ulist, dlist = create_inital_address2(word,2013,12)
        with open('address2017-01-09.txt','a') as file:
            for item in ulist:
                file.write(item+'\n')

        with open('date2017-01-09.txt','a') as file:
            for item in dlist:
                file.write(item+'\n')




def main3():
    # keyword_list = ['扯淡', '腹黑', '接地气', '闷骚', '完爆', '正能量', '达人']
    keyword_list = ['淡定', '纠结', '山寨', '吐槽','自拍']
    for key in keyword_list:
        file_list = util.get_file_list(r"D:\semantic analysis\纯文本\新词//"+key,".txt")
        date_list = []
        for file_name in file_list:
            date_list.append(file_name[:-4])
        urlList,dateList = create_inital_address3(key,date_list)
        with open("url_list.txt","a") as f:
            for url in urlList:
                f.write(url+"\n")

main1()