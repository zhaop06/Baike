# -*- coding: utf-8 -*-
"""

Spyder Editor   
This is a temporary script file.  

"""

import time
import codecs
import SpiderTaskMysql


datetime = "2016-03-01"
table = SpiderTaskMysql.SpiderMysql("dict")
sql_insert = "insert into wiki (title, content, updateTime) values (%s, %s, %s)"

name = "******\\维基百科.txt"
wikiFile = open(name, 'r', encoding='utf-8')
title = wikiFile.readline()
content = wikiFile.readline()+wikiFile.readline()
flag = table.insert(sql_insert, (title, content, datetime))
Nextline = wikiFile.readline()
flagString = Nextline
count = 1
while (Nextline != ''):
    if Nextline == flagString:
        title = wikiFile.readline()
        content = wikiFile.readline()+wikiFile.readline()
        flag = table.insert(sql_insert, (title, content, datetime))
        Nextline = wikiFile.readline()
        count += 1
        if (count%100 == 0):
            print("入库词条数  %d  条" % count)
    else:
        Nextline = wikiFile.readline()
        continue
wikiFile.close()
table.close()
