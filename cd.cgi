#!/usr/bin/python
import commands
import cgi
import cgitb    #traceback errors on browser

cgitb.enable()

print "Content-Type: text/html"
print ""

mypage_data=cgi.FieldStorage()
dir=mypage_data.getvalue('directory')

print commands.getoutput('cd '+dir)



