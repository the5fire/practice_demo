#coding=utf-8                            #  1      #  1
                                         #  2      #  2
import fileinput                         #  3      #  3
                                         #  4      #  4
for line in fileinput.input(inplace=True): #  5    #  5
    line = line.rstrip()                 #  6      #  6
    num = fileinput.lineno()             #  7      #  7
    print '%-50s # %2i' % (line,num)     #  8      #  8
