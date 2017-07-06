#!/usr/bin/python
print 'content-type:text/html \n'
print '<!DOCTYPE html><head><title>School</title></head><body style="background-color:#ccffe6;">'

import cgi
import cgitb
import gameLibFunctions

cgitb.enable()

query=cgi.FieldStorage()
userName=query['ooser'].value

openstring1='dirOfAccounts/a' + userName + '.txt'
openstring2='secondaryDir/a' + userName + '.txt'

primaryPyDict=gameLibFunctions.getRecentDict(openstring1)
secondaryPyDict=gameLibFunctions.getRecentDict(openstring2)


if float(primaryPyDict['energy']) < 50:
    print 'You do not have enough energy left to attend school<br>'
else:
    
    print 'You have ' + primaryPyDict['energy'] + ' units of energy left in your battery'
    print '<br>Your intelligence is rated at ' + secondaryPyDict['intellect']
    print '<br>Going to school can help you get a better job, but consumes a lot of energy'
    
    print '<form action="school.py" method="POST">'
    print '<input type="hidden" name="ooser" value="' + userName + '">'
    print '<input type="submit" name="ToSchool" value="goToSchool"></form>'

    
    
if 'ToSchool' in query:
    secondaryPyDict['intellect']=str(float(secondaryPyDict['intellect']) + 1)
    primaryPyDict['energy']=str(float(primaryPyDict['energy']) - 50)
    secondaryWriteString=secondaryPyDict['intellect'] + ',' + secondaryPyDict['inventory'] + '\n'
    primaryWriteString=primaryPyDict['lastLogin']+','+primaryPyDict['robohashLink'] + ',' + primaryPyDict['energy'] + ',' + primaryPyDict['speed'] + ',' + primaryPyDict['attack'] + ',' + primaryPyDict['defence'] + ',' + primaryPyDict['money'] + ',' + primaryPyDict['level'] + ',' + primaryPyDict['hp'] + '\n'
    f=open(openstring1,'a')
    f.write(primaryWriteString)
    f.close()
    f=open(openstring2,'a')
    f.write(secondaryWriteString)
    f.close()

print '<form action="town.py" method="POST">'
print '<input type="hidden" name="ooser" value="' + userName + '">'
print '<input type="submit" name="submit" value="Return to town"><br>'
print '<img src="http://assets.nydailynews.com/polopoly_fs/1.1105033.1341006443!/img/httpImage/image.jpg_gen/derivatives/landscape_635/bukiet1e-1-web.jpg">'
print '</body></html>'
