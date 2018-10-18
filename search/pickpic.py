# -*- coding: utf-8 -*-
import os
import sys
import re

def pickuppic(directory,outdirectory,suffix):
    for root,dir,files in os.walk(directory):
        fcount = 0
        for file in files:
            #print("type:%s,name:%s" % (type(file),file))
            #print("find file %s" % (type(re.search(suffix,file))))
            #print(os.path.splitext(file))
            if os.path.splitext(file)[1] == suffix:
                newfilename = outdirectory + str(fcount) + suffix
                oldfilename = directory + file
                newfile = open(newfilename,"wb")
                oldfile = open(oldfilename,"rb")
                fcount = fcount + 1
                try:
                    while True:
                        newfile.write(next(oldfile))
                except StopIteration as SI:
                    print("文件读取结束！")
                    newfile.close()
                    oldfile.close()

            #print("type:%s,content:%s" % (type(filename.string),filename.string))


if __name__ == '__main__':
    #dir = input("要筛选的目录：")
    #print(dir)
    #outdir = input("目标目录：")
    #outdir = os.getcwd() + '/' + outdir + '/';
    #print(outdir)
    dir =  os.getcwd() + "/licenseplates/"
    outdir = os.getcwd() + '/out/'

    if not os.path.exists(outdir):
        os.mkdir(outdir)
        print("成功创建文件夹！！！")

    suffix = input("要挑选的后缀：")

    pickuppic(dir,outdir,suffix)
