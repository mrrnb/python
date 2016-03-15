#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import MySQLdb

db = MySQLdb.connect(host = "localhost",user = 'root',passwd = '123',db = 'rrdb')
cursor = db.cursor()

cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print "Database version : %s" %data

cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
sql = """CREATE TABLE EMPLOYEE(
        FIRST_NAME CHAR(20) NOT NULL,
        LAST_NAME CHAR(20),
        AGE INT,
        SEX CHAR(1),
        INCOME FLOAT)"""
cursor.execute(sql)

sql1 = """INSERT INTO EMPLOYEE(
        FIRST_NAME,LAST_NAME,AGE,SEX,INCOME)
        VALUES ('Mac','Mohan',20,'M',2000)"""
sql2 = """INSERT INTO EMPLOYEE(
        FIRST_NAME,LAST_NAME,AGE,SEX,INCOME)
        VALUES ('%s','%s','%s','%s','%s')"""%\
        ('Ez','real',22,'W',20000)
try:
    cursor.execute(sql1)
    cursor.execute(sql2)
    db.commit()
except:
    db.rollback()

sql3 = "SELECT * FROM EMPLOYEE \
        WHERE INCOME> '%d'" %(1000)
try:
    cursor.execute(sql3)
    results = cursor.fetchall()
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        print "fname=%s, lname=%s, age=%d, sex=%s, income=%d" %\
                (fname,lname,age,sex,income)
except:
    print "Error: unable to fetch data"

sql4 = "UPDATE EMPLOYEE SET AGE = AGE + 1\
        WHERE SEX = '%s'" %('M')
try:
    cursor.execute(sql4)
    db.commit()
except:
    print "Error, Updata will be rollback!"
    db.rollback()

db.close()

