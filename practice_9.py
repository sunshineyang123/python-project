#!/usr/bin/python
# -*- coding: UTF-8 -*-
#暂停一秒输出
 
import time
 
myD = {1: 'a', 2: 'b'}
for key, value in dict.items(myD):
    print key, value
    time.sleep(1) # 暂停 1 秒

