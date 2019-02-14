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

name = data.getvalue("uname")

password = data.getvalue("passwd")



query="SELECT username,password FROM users" 
c.execute(query)
data=c.fetchall()

for i in range (0,len(data)):
	if data[i][0] ==  name:
		if data[i][1] == password:
			print data[i]
		else:
			print "Wrong Password entered"
		
	else:
		print "The username does not exist"

connection.close()
