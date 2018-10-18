# -*- coding: utf-8 -*-
import re  
import requests
import os
import ctypes
import sys

def downloadPic(html,keyword,pn ,savepath):
    i = 0
    pic_url = re.findall('"objURL":"(.*?)",',html,re.S)#找到网站中每个图片的url,最后存储到列表里
    m_s = '找到关键词:' + keyword + '的图片，现在开始下载图片...'
    print(m_s)
    for each in pic_url:
        sys.stdout.write(u"现在正在下载第%s张图片，图片地址:%s\n" % (str(i+1),str(each)))
        #print 'downloading...'
        try:  
            pic= requests.get(each, timeout=50)  
        except  Exception as ex :
            print('【错误】当前图片无法下载')
            continue

        #print("head = %s" % (str(pic.headers)))
        pic_url_list = re.split('/',each)
        pic_name_list = re.split('\.',pic_url_list[-1])
        pic_suffix = pic_name_list[-1]

        pic_new_name = str('%s/%s.%s' % (savepath , str('%d_%d' % (pn,i)) , pic_suffix))
        #pic_new_name = str("%s/%s" % (savepath,))
        
        print(pic_new_name)
        #resolve the problem of encode, make sure that chinese name could be store
        fp = open(pic_new_name,'wb')
        fp.write(pic.content)#response.content以二进制形式返回爬取的内容
        fp.close()
        i += 1




if __name__ == '__main__':
    word =  input('Input keywords:')
    #url = 'http://image.baidu.com/s
    # earch/flip?tn=baiduimage&ie=utf-8&word='+word+'&ct=201326592&v=flip'
    pnMax = int(input('Input max pn:'))
    filepath = input('Input save dir:')
    currentpath = os.getcwd()
    filepath = currentpath + '/' + filepath

    pncount = 0  
    gsm = 80   
    str_gsm =str(gsm)

    if not os.path.exists(filepath):
        os.mkdir(filepath)

    print(filepath)
    for list in os.walk(filepath):
        for file in list[2]:
            rp = '%s/%s' % (filepath,file)
            print('remove file %s' % (rp))
            os.remove(rp)
        #os.remove(file)
        #print u'成功删除文件%s' % (file)

    while pncount<pnMax:  
        str_pn = str(pncount)  
        url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word='+word+'&pn='+str_pn+'&gsm='+str_gsm+'&ct=&ic=0&lm=-1&width=0&height=0'  
        result = requests.get(url)#爬取一个百度图片网站
        print('url%d:%s' % (pncount,url))
        print(u'打开文件 %s%d.txt' % (filepath,pncount))

        fd = os.open("%s/%d.txt" % (filepath,pncount),os.O_WRONLY|os.O_CREAT)
        c_s = ("result.txt: %s\n ----------------------------------------------  \n" % (result.text))
        os.write(fd,c_s.encode("utf-8"))#response.text以uft-8编码形式返回爬取的数据
        os.close(fd)

        pncount = pncount + 1
        downloadPic(result.text,word,pncount ,filepath)
    print('下载完毕')

