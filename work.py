#!/usr/bin/python
print 'content-type:text/html \n'

import cgi
import cgitb
import gameLibFunctions

cgitb.enable()

query=cgi.FieldStorage()
userName=query['ooser'].value

print '<!DOCTYPE html><head><title>Work</title></head><body style="background-color:#ffe6b3;">'

openstring='dirOfAccounts/a' + userName + '.txt'
openstring2='secondaryDir/a' + userName + '.txt'

primaryDict=gameLibFunctions.getRecentDict(openstring)
secondaryDict=gameLibFunctions.getRecentDict(openstring2)

print 'The amount of money you have now is ' + primaryDict['money'] + '<br>'
print 'The amount of battery left in you is ' + primaryDict['energy'] + '<br><br>'

def formJobMaker(buttonValue,energyCost,userName,moneyMade):
    print '<form action="work.py" method="GET">'
    print '<input type="hidden" name="ooser" value="' + userName + '">'
    print '<input type="submit" name="' + buttonValue + '" value="' + buttonValue+'">'
    print '<br>This job costs ' + str(energyCost) + ' energy to do' + '<br>'
    print 'This job will return ' + str(moneyMade) + ' bolts for your effort<br><br>'
    print '</form>'

if float(primaryDict['energy']) >= 25:
    formJobMaker('mow_some_lawns',25,userName,25)
else:
    print 'not enough energy to do mow lawns <br><br>'

if float(primaryDict['energy']) >=35 and float(secondaryDict['intellect']) >= 55:
    formJobMaker('teach_high_school_kids_computer_science',35,userName,55)
elif float(primaryDict['energy']) >=35:
    print 'You need 55 intellect to teach computer science man<br><br>'
else:
    print 'You need 35 energy to teach computer science man bro<br><br>'

if float(primaryDict['energy']) >= 40 and float(secondaryDict['intellect']) >= 80:
    formJobMaker('install_yourself_into_a_spaceship_yard',40,userName,175)
elif float(primaryDict['energy']) >=40:
    print 'You need 80 intellect to install yourself into a spaceship yard<br><br>'
else:
    print 'You need 40 energy to install yourself into a spaceship yard<br><br>'

print '<form action="town.py" method="POST">'
print '<input type="hidden" name="ooser" value="' + userName + '">'
print '<input type="submit" name="submit" value="head to town"></form>'

if 'mow_some_lawns' in query:
    primaryDict['energy']=str(float(primaryDict['energy'])-25)
    primaryDict['money'] = str(float(primaryDict['money']) + 25)

if 'teach_high_school_kids_computer_science' in query:
    primaryDict['energy']=str(float(primaryDict['energy'])-35)
    primaryDict['money'] = str(float(primaryDict['money']) + 55)
	
if 'install_yourself_into_a_spaceship_yard' in query:
    primaryDict['energy']=str(float(primaryDict['energy'])-40)
    primaryDict['money'] = str(float(primaryDict['money']) + 80)
	
primaryWriteString=primaryDict['lastLogin']+','+primaryDict['robohashLink'] + ',' + primaryDict['energy'] + ',' + primaryDict['speed'] + ',' + primaryDict['attack'] + ',' + primaryDict['defence'] + ',' + primaryDict['money'] + ',' + primaryDict['level'] + ',' + primaryDict['hp'] + '\n'

f=open(openstring,'a')
f.write(primaryWriteString)
f.close

print '<img src="http://cache2.asset-cache.net/gc/165502693-octopus-robot-renovation-gettyimages.jpg?v=1&c=IWSAsset&k=2&d=oa8U95Qw0%2Fjo2A4YhBrBDlSLddYTdv0NdTaz%2FV9WxX29kHiDATtkLHneTykp4cc7">'
print '</body></html>'
