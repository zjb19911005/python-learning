
#coding=utf-8
# __author__ = 'Junior'
imoort MySQl
conn = MySQldb.connect(host='rdst5ai4d32fe3qd6if46public.mysql.rds.aliyuncs.com', port='3306', user='qgd_stf_wt_qa',
                       passwd='NPzMwpzYVobbCYBSlv6M', charset='utf8', connect_timeout=20)
cursor = conn.cursor()
sql = 'select * from trade WHERE shop_identy=810004909'
cursor.execute(sql)  # 执行sql语句
alldata = cursor.fetchall()
cursor.close()
conn.close()
print alldata[0][0].encode('UTF-8')
