__author__ = 'Junior'
s = "www.jeapedu.com"
print s[ 10:-12:-1]
x = 10
while x <= 300:
    x = x + 10
    sb = "http://www.baidu.com/s?wd=latex&pn="+str(
    x)+"&tn=baiduhome_pg&ie=utf-8&usm=1"
print sb
s = "www.jeapedu.com"
b = s.find('j')
e = s.find('.', b)
print s[b : e]

s = "www.jeapedu.com"
b = s.find('j')
print b
print(s[:b])
print(s[b+1:])
s=s[:b]+'J'+s[b+1:]
print s


s="www.keryunwoaoni.com"
s1=s.replace('w','W',2)
print s1

import webbrowser as web
import  os
import time
import

i=1
for i in range(10):
    url='http://erp.keruyun.com/login.jsp'
    web.open_new_tab(url)
    time.sleep(1)
    SendKeys.SendKeys("^{F5}")
    time.sleep(1)
os.system('taskkill /F /IM chrome.exe')