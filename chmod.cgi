#!/usr/bin/python

import cgi
import cgitb

import commands

cgitb.enable()

print "Content-Type:text/html"
print ""

mypage_data=cgi.FieldStorage()
who=mypage_data.getvalue('who')
what=mypage_data.getvalue('what')
which=mypage_data.getvalue('which')
file=mypage_data.getvalue('file')
if(what=='add'):
	com=who+'+'+which
if(what=='remove'):
	com=who+'-'+which
print "<pre>"
print commands.getoutput("sudo chmod "+com+' '+file)


print "</pre>"
print "\n \n"

print '<a href="/linuxGUI/home.html">'
print 'Back to Home Page'
print '</a>'
