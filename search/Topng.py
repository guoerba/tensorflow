# -*- coding: utf-8 -*-
import cv2
import os

if __name__ == "__main__":
    inputdir = input("输入目录:")
    outputdir = input("输出目录：")
    #inputdir = os.getcwd() + "/licenseplates/"
    #outputdir = os.getcwd() + "/outpng/"
    if not os.path.exists(outputdir):
        os.mkdir(outputdir)
        print("创建目录%s" % (outputdir))
    for root,dir,files in os.walk(inputdir):
        #print('root:%s,dir:%s,files:%s' % root,dir,files))
        count = 0
        for file in files:
            try:
                inputimg = inputdir + file
                print("正在转换第%d幅图%s" % (count,inputimg))
                img = cv2.imread(inputimg)
                #cv2.imshow(file,img)
                cv2.imwrite(outputdir + str(count) + "car.png",img)
                count = count + 1
               # break
            except:
                print("发生了不可能的事情！！！")
                exit(1)