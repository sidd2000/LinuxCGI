#!/usr/bin/python
import cgi
import cgitb
#import commands
import pymysql.cursors 

connection = pymysql.connect(host='localhost',db='webdb',user='webuiuser',password='')
c = connection.cursor()
print "Content-type:text/html"
print ""

data=cgi.FieldStorage()

name = data.getvalue("suname")
username= data.getvalue("suuname")
password = data.getvalue("supass")



query='INSERT INTO users(name,username,password) VALUES('+name+','+username+','+password+');'
c.execute(query)
data=c.fetchall()

#for i in range (0,len(data)):
#	if data[i][0] ==  name:
#		if data[i][1] == password:
#			print data[i]
print data

connection.close()
