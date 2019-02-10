#!/usr/bin/python
import commands
import cgi
import cgitb    #traceback errors on browser

cgitb.enable()

print "Content-Type: text/html"
print ""

mypage_data=cgi.FieldStorage()

string= commands.getoutput('sudo dumpe2fs /dev/sda1 | grep "Filesystem created:"')
index=string.find(':')+5
string=string[index:]
print "<pre>"
print string
print "</pre>"
print "\n \n"

print '<a href="/linuxGUI/home.html">'
print 'Back to Home Page'
print '</a>'
