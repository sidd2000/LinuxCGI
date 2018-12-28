#!/usr/bin/python

import commands
import cgi
import cgitb

cgitb.enable()

print "Content-Type:text/html"
print ""

mypage_data=cgi.FieldStorage()
directory=mypage_data.getvalue('directory')

print commands.getoutput('mkdir -p '+directory)

~                                  
