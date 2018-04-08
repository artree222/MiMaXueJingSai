# coding=utf-8

import codecs
f = codecs.open(u'C:\\Users\\zhang\\Desktop\\密码竞赛\\题目\\知识.txt','r','utf-8')
lines = f.readlines()
f.close()
f = codecs.open(u'C:\\Users\\zhang\\Desktop\\密码竞赛\\知识.csv','w','utf-8')
print(len(lines))

#一行中的数据
row = []
for line in lines:
    line = line.strip('\r\n')
    if line=="":
        f.write("|".join(row)+"\r\n")
        row = []
    else:
        row.append(line)
        
