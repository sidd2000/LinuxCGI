#!/usr/bin/python

import cgi
import cgitb
import commands
cgitb.enable()

print "Content-Type:text/html"
print ""

mypage_data=cgi.FieldStorage()
directory=mypage_data.getvalue('directory')

print commands.getoutput('mkdir -p '+directory)

~                                  
