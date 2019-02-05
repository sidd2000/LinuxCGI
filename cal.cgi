#!/usr/bin/python

import cgi
import cgitb

import commands

cgitb.enable()

print "Content-Type:text/html"
print ""

mypage_data=cgi.FieldStorage()
month=mypage_data.getvalue('month')
year=mypage_data.getvalue('year')


if month is None:
        month=' '
if year is None:
        year=' '
print "<pre>"
print commands.getoutput("cal "+month+" "+year)

print "</pre>"
print "\n \n"

print '<a href="/linuxGUI/home.html">'
print 'Back to Home Page'
print '</a>'
