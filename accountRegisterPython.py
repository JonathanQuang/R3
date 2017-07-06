#!/usr/bin/python
print 'content-type:text/html \n'

import cgi
import cgitb
import os
import codeify
import random
import time

cgitb.enable()

print '<!DOCTYPE html><html><head></head><body>'

query=cgi.FieldStorage()

if not('theUser' in query and 'thePass' in query and 'thePassRepeat' in query):
        print "Please fill in all fields"
        print '<a href="register.html">click here to go back and register</a>'
        print '</body></html>'
        exit()

userName = query['theUser'].value
passWord =  query['thePass'].value
passWordRepeat = query['thePassRepeat'].value
theEmail = query['theEmail'].value



g = open('accounts.txt')
s = g.read()
s = s.strip()
s = s.split('\n')
g.close()


dictionList={}
for x in s:
	x=x.split(',')
	dictionList[x[0]] = x[1:]

listOfEmails=[]
for x in dictionList.values():
	listOfEmails.append(x[1])

gobackString='<a href=register.html>Try again</a>'

        
if not(userName in dictionList):
	if passWord == passWordRepeat:
		if not(theEmail in listOfEmails):
			g=open('accounts.txt','a')
			g.write(userName + ',' + codeify.superHasher(passWord,userName) + ',' + theEmail + '\n')
			g.close()
                        openstring='dirOfAccounts/' + 'a' + userName + '.txt'
                        p=os.open(openstring,os.O_RDWR|os.O_CREAT)
                        os.close(p)
                        os.chmod(openstring,0666)
                        f=open(openstring,'w')
                        f.write('lastLogin,robohashLink,energy,speed,attack,defence,money,level,hp\n')
                        timeOfLogin=time.localtime()
                        f.write(str(timeOfLogin[7]) + ',' + 'https://robohash.org/' + userName + '.png' + ',' + '100,10,5,5,100,1,50\n')
                        f.close()
                        
                        secondOpenString='secondaryDir/' + 'a' + userName + '.txt'
                        
                        p=os.open(secondOpenString,os.O_RDWR|os.O_CREAT)
                        os.close(p)
                        os.chmod(secondOpenString,0666)
                        
                        f=open(secondOpenString,'w')
                        f.write('intellect,inventory\n')
                        f.write('10,null\n')
                        
			print 'register success'
                        print '<a href=account.html>Go login now</a>'
		else:
			print 'email in use'
                        print gobackString
	else:
		print 'passwords do not match'
                print gobackString
else:
	print 'username already taken'
        print gobackString



print '</body></html>'



