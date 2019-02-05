#!/usr/bin/python
import commands
import cgi
import cgitb    #traceback errors on browser

cgitb.enable()

print "Content-Type: text/html"
print ""

mypage_data=cgi.FieldStorage()

print "<pre>"
print commands.getoutput('echo $0')

print "</pre>"
print "\n \n"

print '<a href="/linuxGUI/home.html">'
print 'Back to Home Page'
print '</a>'

