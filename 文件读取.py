#coding=utf-8
__author__ = 'Junior'
contact='/Users/Junior.Zhu/Desktop/备用文本.txt'
phone=open(contact,'w+')
phone.write('%5s\t %3s\t %6s\n' %('name','age','sex'))
phone.write('%5s\t %3s\t %6s\n' %('zhu','17','male'))
phone.write('%5s\t %3s\t %6s\n' %('jun','18','male'))
phone.write('%5s\t %3s\t %6s\n' %('bo','19','male'))
phone.close()
phone1=open(contact,'r+')
r=phone1.readline(10).strip().strip('\n')
print r