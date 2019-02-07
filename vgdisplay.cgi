#!/usr/bin/python
import commands
import cgi
import cgitb    #traceback errors on browser

cgitb.enable()

print "Content-Type: text/html"
print ""

mypage_data=cgi.FieldStorage()
name=mypage_data.getvalue('name')

if name is None:
	print "You must enter a name"
else:
	print "<pre>"
	print commands.getoutput('sudo vgdisplay '+name)
	print "</pre>"
print "\n \n"

print '<a href="/linuxGUI/home.html">'
print 'Back to Home Page'
print '</a>'

