# coding=utf-8

import codecs
f = codecs.open(u'C:\\Users\\zhang\\Desktop\\密码竞赛\\题目\\判断题.txt','r','utf-8')
lines = f.readlines()
f.close()
f = codecs.open(u'C:\\Users\\zhang\\Desktop\\密码竞赛\\判断题.csv','w','utf-8')
print(len(lines))


#一行中的数据
row = []
i = 0
while i < len(lines):
    line1 = lines[i].strip("\r\n")
    i = i +1
    line2 = lines[i].strip("\r\n")
    f.write(line1+"|"+line2+"\r\n")
    i = i+1
f.close()
