#!/usr/bin/python
print 'content-type:text/html \n'
print'<!DOCTYPE html><html><head><title>Town</title></head><body background="http://api.ning.com/files/DtcI2O2Ry7A5ZJ2m1YROlwvwcBW5D8*x1I-wLs8L5uFVxIynS4OPz6UENhrcnKBin-5vqEQoF*KNcQ8S8KBuhIDll0-1P4-K/1082125932.jpeg" style="background-repeat:no-repeat;background-size:cover">'

import cgi
import cgitb
import codeify
import gameLibFunctions
import os

cgitb.enable()

query=cgi.FieldStorage()
userName=query['ooser'].value
buttonTest=query['submit'].value


openString= 'dirOfAccounts/a' + userName + '.txt'
f=open(openString)
s=f.read()
f.close()

pyDict = gameLibFunctions.getRecentDict(openString)


print '<img src="' + pyDict['robohashLink'] + '">'
print '<br><b>' + 'Battery:' + pyDict['energy']
print '<br>' + 'Bolts:' + pyDict['money'] + '</b>'
print '<center><h1 style="position:absolute;top:0;background-color:#80dfff;"> Welcome to Robotville ' + userName + ' </h1></center>'
print '<form action="game.py" method="POST">'
print '<input type="hidden" name="ooser" value="' + userName + '"/>'
print '<input type="submit" name="home" value="Head home"/></form>'
print '<form action="arena.py" method="POST">'
print '<input type = "hidden" name ="ooser" value="' + userName + '"/>'
print '<input type="submit" name="arena" value="Head to the arena"/></form>'
print '<form action="planetfitness.py" method="POST">'
print '<input type = "hidden" name = "ooser" value="' + userName + '"/>'
print '<input type = "submit" name ="submit" value="head to the gym"></form>'
print '<form action="school.py" ethod="POST">'
print '<input type="hidden" name = "ooser" value="' + userName + '"/>'
print '<input type = "submit" name = "submit" value="Head to school"></form>'
print '<form action="work.py" method="POST">'
print '<input type = "hidden" name="ooser" value="' + userName + '"/>'
print '<input type= "submit" name = "submit" value = "Head to work"></form>'
print '<form action = "store.py" method = "POST">'
print '<input type = "hidden" name = "ooser" value="' + userName + '"/>'
print '<input type = "submit" name = "submit" value = "Head to the store"></form>'


accounts=os.listdir('dirOfAccounts')
counter = 0
accountsNoDupe=[]




for x in accounts:
     if x.find('~') > -1:
         x=x[1:len(x)-5]
         accountsNoDupe.append(x)



TopAccount=''
TopLevel=0
TopSecond=''
SecondLevel=0
TopThird=''
ThirdLevel=0



for x in accountsNoDupe:
    name=x
    x=gameLibFunctions.getRecentDict('dirOfAccounts/a' + x + '.txt')
    if float(x['level']) >= float(TopLevel):
        TopThird=TopSecond
        ThirdLevel=SecondLevel
        TopSecond=TopAccount
        SecondLevel=TopLevel
        TopAccount=name
        TopLevel=x['level']
    elif float(x['level']) >= float(SecondLevel):
        TopThird=TopSecond
        ThirdLevel=SecondLevel
        TopSecond=name
        SecondLevel=x['level']
    elif float(x['level']) >= float(ThirdLevel):
        TopThird=name
        ThirdLevel=x['level']

print '<div style="background-color:white;width:50%;position:relative;left:50%;">'
print '<h2 style="text-align:right;"> The Gov of Robotville is run by the three most powerful robots.<br> In the event of a tie, python weirdness shall determine who wins'
print '<br>The Head Dictator is ' + TopAccount + ' with a level of '+ TopLevel
print '<br>Second in Command is ' + TopSecond + ' with a level of ' + SecondLevel
print '<br>Third in Command is ' + TopThird + ' with a level of '+ ThirdLevel
print '</div></h2></body></html>'
