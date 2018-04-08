#coding=utf-8

import codecs

f = codecs.open(u'C:\\Users\\zhang\\Desktop\\密码竞赛\\题目\\比赛多选题收集(可能不全)[格式较混乱].txt','r','utf-8')
#f = codecs.open(u'C:\\Users\\zhang\\Desktop\\密码竞赛\\题目\\单选汇总.txt','r','utf-8')
lines = f.readlines()
f.close()
timus = []
f = codecs.open(u'C:\\Users\\zhang\\Desktop\\密码竞赛\\多选题.csv','w','utf-8')
i = 0
while i<len(lines):
    timu = lines[i].strip('\r\n')
    i = i+1
    xuanXianA = lines[i].strip('\r\n')
    i = i+1
    xuanXianB = lines[i].strip('\r\n')
    i = i+1
    xuanXianC = lines[i].strip('\r\n')
    i = i+1
    xuanXianD = lines[i].strip('\r\n')
    i = i+1
    daAn = lines[i].strip('\r\n')
    i = i+1
    sss = timu+u"|"+xuanXianA+u"|"+xuanXianB+u"|"+xuanXianC+u"|"+xuanXianD+u"|"+daAn
    
    if(timu in timus):
        print timu
    timus.append(timu)
    f.write(sss)
    f.write('\r\n')
    #print sss
f.close()