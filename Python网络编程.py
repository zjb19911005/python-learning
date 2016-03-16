#coding=utf-8
__author__ = 'Junior'
import urllib,urllib2
#response=urllib.urlopen('http://www.baidu.com/')
#html= response.read()
#print html

url ='http://music.baidu.com/song/260396428/download?__o=%2Fartist%2F31514359'
r =urllib2.urlopen(url)
data= r.read()
with open('我带外地去看你.mp3','wb') as code:
    code.write(data)
urllib.urlretrieve(url,'test.mp3')