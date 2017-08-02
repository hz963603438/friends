#! /usr/bin/env python3
# coding:utf-8

from mysql.connector import connect


db_config = { 'host':'localhost',
       'port':3306,
       'user':'root',
       'password':'ucheck2016',
       'db':'mysql',
}

cnn = connect(**db_config)
cur = cnn.cursor()

sql_1 = '''
create table from_connector(
  id int primary key auto_increment,
  name varchar(20) not null
)
'''
sql_2 = '''
show tables
'''
cur.execute(sql_1)
res1 = [i for i in cur]
print (res1)
cur.execute(sql_2)
res2 = [i for i in cur]
print (res2)
for i in cur:
    print (i)

cur.close()
cnn.close()
