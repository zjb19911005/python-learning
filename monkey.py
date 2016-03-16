#coding=utf-8
__author__ = 'Junior'


import os
import time
import random
import re

#os.popen('adb install /Users/Junior.Zhu/Desktop/APK/6.4.0/KeruyunCalm3_V6.4.0Relea.apk').readlines()
#print'执行Monkey脚本'
#output = os.popen('adb shell monkey -p com.shishike.calm --pct-touch 50 --pct-trackball 20 -s 10 --throttle 200 -v %d' %(random.randint(50000,100000))).read()   #请手动替换-p参数后面的apk包名
#pattern = re.compile(r'FatalException', re.IGNORECASE)
#result = pattern.findall(output)
#if len(result) > 0:
#    dt = time.strftime('%Y-%m-%d-%H-%M-%S')
#    logfilename = "log_"  "_" + dt
#    input = open('/Users/Junior.Zhu/Desktop/备用文本.txt'+logfilename+dt, 'w')
#    input.write('执行monkey时发生crash，日志：')
#    input.writelines(output)
#    input.close()
#    print '执行monkey时发生异常'
#print '测试完成，卸载'
#os.popen('adb uninstall com.shishike.calm')  # 请手动替换后面的apk包名


apks=[]
for x in os.listdir('/Users/Junior.Zhu/Desktop/APK/6.4.0/'):
   if os.path.abspath(x) and os.path.splitext(x)[1] == '.apk':
    apks.append(x)
for apk in apks:
    print '安装'+apk
    os.popen('adb devices').readlines()
#    os.popen('monkey start')
    os.popen('adb install /Users/Junior.Zhu/Desktop/APK/6.4.0/'+apk).readlines()
    print '执行Monkey脚本'
    output = os.popen('adb shell monkey -p com.shishike.calm --pct-touch 50 --pct-trackball 20 -s 10 --throttle 200 -v %d' %(random.randint(1000,2000))).read()   #请手动替换-p参数后面的apk包名
    pattern = re.compile(r'crash',re.IGNORECASE)
    result = pattern.findall(output)
    if len(result)>0:
        dt = time.strftime('%Y-%m-%d-%H-%M-%S')
        logfilename = "log_"+apk.split('.apk')[0]+"_"+dt
        input = open('/Users/Junior.Zhu/Desktop/log/'+logfilename+'.log','w')
        input.write(apk+'执行monkey时发生crash，日志：')
        input.writelines(output)
        input.close()
        print apk+':执行monkey时发生异常'
    print '测试完成，卸载'+apk
    os.popen('adb uninstall com.shishike.calm')
print'Monkey跑完了,请查看log'