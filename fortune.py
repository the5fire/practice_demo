#coding=utf-8

import  fileinput, random

fortunes = list(fileinput.input())
print random.choice(fortunes)
