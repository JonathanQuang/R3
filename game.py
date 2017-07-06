#!/usr/bin/python
print 'content-type:text/html \n'
print '<!DOCTYPE html><html><head><title>Home</title><link rel="stylesheet" type="text/css" href="style.css"></head>\n<body background="http://previews.123rf.com/images/benchart/benchart1301/benchart130100022/17378900-Illustration-of-a-cartoon-home-interior-room-or-office-with-wood-flooring-ground-and-empty-green-str-Stock-Vector.jpg">'

import cgi
import cgitb
import gameLibFunctions

cgitb.enable()


query=cgi.FieldStorage()
userName=query['ooser'].value

f=open('dirOfAccounts/' + 'a' + userName + '.txt')
r=f.read()
r=r.strip()
f.close()
gameLibFunctions.updateEnergy('dirOfAccounts/' + 'a' + userName + '.txt')
r=r.split('\n')
pyDict={}



lastLogin = r[len(r) - 1]
lastLogin= lastLogin.split(',')
titles=r[0]
titles=titles.split(',')
counter = 0

secondaryDict=gameLibFunctions.getRecentDict('secondaryDir/a' + userName + '.txt')

for something in titles:
	pyDict[something] = lastLogin[counter]
        counter += 1

        
print '<center>'
print '<img src="' + pyDict['robohashLink']+ '">'
print '<table border="1" bgcolor="#a9e788" ><tr><th>Battery Life</th><td>' + pyDict['energy'] + '</td></tr>'
print '<tr><th>AttackPwr</th><td>' + pyDict['attack'] + '</td></tr>'
print '<tr><th>Force Field Capacity</th><td>' + pyDict['defence'] + '</td></tr>'
print '<tr><th>Speed</th><td>' + pyDict['speed'] + '</td><tr>'
print '<tr><th>Bolts</th><td>' + pyDict['money'] + '</td></tr>'
print '<tr><th>Level</th><td>' + pyDict['level'] + '</td></tr>'
print '<tr><th>Armor/HP</th><td>' + pyDict['hp'] + '</td></tr>'
print '<tr><th>Intelligence</th><td>' + secondaryDict['intellect'] + '</td></tr>'
print '</table>'

print '<form action = "town.py" method = "POST"">'
print '<input type="hidden" name = "ooser" value ="' + userName + '">'
print '<input type = "submit" name = "submit" value = "head to town"></form>'
print '</center>'
print '<center><a href="account.html">Logout</a></center>'


print '</body></html>'


