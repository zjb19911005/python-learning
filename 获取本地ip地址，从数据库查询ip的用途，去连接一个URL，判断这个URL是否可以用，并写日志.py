#coding=utf-8
__author__ = 'Junior'
import os,urllib,MySQldb,time,platform
def log_w(text):
    logfile='/tmp/wbsocket.log'
    if os.path.isfile(logfile):
        if(os.path.getsize(logfile)/1024/1024)>100:
            os.remove(logfile)
    now =time.strftime('%Y-%m-%d %H:%M:%s')
    tt =str(now)+'\t'+str(text)+'\n'
    f=open(logfile,'a+')
    f.write(tt)
    f.close()
def get_idcname(ip):
    try:
        conn=MySQldb.connect(host='rdst5ai4d32fe3qd6if46public.mysql.rds.aliyuncs.com',port='3306',user='qgd_stf_wt_qa',passwd='NPzMwpzYVobbCYBSlv6M',charset='utf8',connect_timeout=20)
        cursor=conn.cursor()
        sql='select * from trade WHERE shop_identy=810004909'
        cursor.execute(sql)#执行sql语句
        alldata=cursor.fetchall()
        cursor.close()
        conn.close()
        return alldata[0][0].encode('UTF-8')
    except Exception:
        return 0

def get_ip():
    os =platform.system()
    if os =='Linux':
        ip =os.popen("/sbin/ipconfig eth0|grep 'inet addr'").read().strip().split(':')[1].split()[0]
    elif os == 'Windows':
        import wmi
        c=wmi.WMI()
        network=c.Win32_NetworkAdapterConfiguration (IPEnabled=1)
        for interface in network:
            if interface.DefaultIPGateway:
                ip=interface.IPAddress[0]
                return ip#print interface.IPAddress[0],interface.MACAddress,interface.IPSubnet[0],interface.DefaultIPGateway[0],interface.DNSServerSearchOrder[0],interface.DNSServerSearchOrder[1]
                #获取出网的ip地址、MAC地址、子网掩码、默认网关、DNS
def web_status():
    ip =get_ip()
    idc_name=get_idcname(ip)
    url ='http://www.text.com/index.php?idc_ip=%s&%idc_name=%s' %(ip,idc_name)
    get =urllib.urlopen(url)
    if get.getcode()==200:
        aa=int(get.read().strip())
        if aa==1:
            text ='Webservice return OK'
        else:
            text='Webservice return Error'
    else:
        text='Connect webservice Error'
    print text
    log_w(text)
if __name__=='__main__':
    web_status()

