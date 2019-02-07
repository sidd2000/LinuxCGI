#!/usr/bin/python
import commands
import cgi
import cgitb    #traceback errors on browser

cgitb.enable()

print "Content-Type: text/html"
print ""

mypage_data=cgi.FieldStorage()
path= mypage_data.getvalue('path')
if path is None:
	print "You must enter a path"
else:
	print "<pre>"
	print commands.getoutput('sudo pvdisplay '+path)
	print "</pre>"
print "\n \n"

print '<a href="/linuxGUI/home.html">'
print 'Back to Home Page'
print '</a>'


