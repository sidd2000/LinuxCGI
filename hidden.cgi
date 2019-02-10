#!/usr/bin/python
import cgi
import cgitb
import commands
cgitb.enable()

print "Content-Type:text/html"
print ""

mypage_data=cgi.FieldStorage()
directory=mypage_data.getvalue('directory')

if directory is None:
        directory=' '

print "<pre>"
print commands.getoutput('ls -d .* '+directory)
print "</pre>"

print "\n \n"

print '<a href="/linuxGUI/home.html">'
print 'Back to Home Page'
print '</a>'

