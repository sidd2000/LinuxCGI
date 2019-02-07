#!/usr/bin/python

import commands
import cgi
import cgitb    #traceback errors on browser

cgitb.enable()

print "Content-Type: text/html"
print ""

mypage_data=cgi.FieldStorage()
command=mypage_data.getvalue('command')

if "reboot" not in command:
	print "<pre>"
	print commands.getoutput(command)
	print "</pre>"
else:
	print "You cannot reboot your PC from this platform"
print "\n \n"

print '<a href="/linuxGUI/home.html">'
print 'Back to Home Page'
print '</a>'

