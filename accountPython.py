#!/usr/bin/python
print 'content-type:text/html \n'
print '<!DOCTYPE html><html><head><title>Login</title>'
print '<link rel="stylesheet" type="text/css" href="style.css"/></head><body id="landingBody">'


import cgi
import cgitb
import codeify

cgitb.enable()

def addUserAndPass(fileName, userName, password):
	f = open(fileName,'a')
	f.write(userName + ',' + password + '\n')
	f.close()

query=cgi.FieldStorage()
userName = query['theUser'].value
passWord =  query['thePass'].value
passWord = codeify.superHasher(passWord,userName)


f=open('accounts.txt')
string=f.read().strip()
f.close()

accountDiction={}
account  = string.split('\n')
for x in account:
        y=x.split(',')
        accountDiction[y[0]]=y[1]

print '<h1 id="Access"><center>'

if userName in accountDiction:
	if accountDiction[userName] == passWord:
		print 'access granted'
                print '<form action="game.py" method="POST" >'
                print '<input type="hidden" name="ooser" value="' + userName + '"/>'
                print '<input type="submit" name="Go to your page" value="verification successful, click here to go to enter your home" id="grant"></form>'
                print '<br><center><img src="http://2.bp.blogspot.com/-OH4QYbShOBE/Ve4cHB-VCcI/AAAAAAABS_o/xnBWkYR43K8/s200/post-63622-dancing-robot-gif-imgur-tumblr-m4jR.gif" id="acceptImage">'
	else:
		print 'access denied password does not match'
else:
	print 'access denied username not found'
        print 'the username you have put is <b>' + userName + '</b>'


print '</h1></center></body></html>'


