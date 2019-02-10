#!/usr/bin/python
import commands
import cgi
import cgitb    #traceback errors on browser

cgitb.enable()

print "Content-Type: text/html"
print ""

mypage_data=cgi.FieldStorage()
uname=mypage_data.getvalue('uname')
upass=mypage_data.getvalue('upass')

if upass is None:
	upass='ubuntu'
if uname is not None:
	user=commands.getoutput('sudo useradd '+uname)
	command= "'"+uname+":"+upass+"'"
	passwd=commands.getoutput("sudo echo %s | sudo chpasswd"%command)

	print "<pre>"
	print user
	print passwd
	print "</pre>"
	print "User Created!"

else:
	print "You cannot leave the username blank"


print "\n \n"

print '<a href="/linuxGUI/home.html">'
print 'Back to Home Page'
print '</a>'

