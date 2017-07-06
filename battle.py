#!/usr/bin/python
print 'content-type:text/html \n'
print '<!DOCTYPE html><html><head></head><body>'

import cgi
import cgitb
import os
import gameLibFunctions
import random

cgitb.enable()

query=cgi.FieldStorage()
userName=query['ooser'].value
enemy=query['Enemy'].value

userDict=gameLibFunctions.getRecentDict('dirOfAccounts/a'+userName+'.txt')
enemyDict=gameLibFunctions.getRecentDict('dirOfAccounts/a'+enemy+'.txt')

originUserDict={}
for x in userDict:
    originUserDict[x]=userDict[x]

userDict.pop('robohashLink')
enemyDict.pop('robohashLink')


for x in userDict:
    userDict[x]=float(userDict[x])

for x in enemyDict:
    enemyDict[x]=float(enemyDict[x])

winner=''
loser=''
    
while (userDict['hp'] > 0) or (enemyDict['hp'] > 0):
    userRandDam=random.randrange(0,userDict['speed']) / 10.0
    enemRandDam=random.randrange(0,enemyDict['speed']) / 10.0
    if userDict['speed'] >= enemyDict['speed']:
       damage=(userDict['attack'] + userRandDam) - (0.5*enemyDict['defence'])
       if damage < 1:
           damage=1
       enemyDict['hp']=enemyDict['hp']-damage
       print enemy + ' was hit for ' + str(damage)+'<br>'
       print enemy + ' has ' + str(enemyDict['hp']) + ' left' + '<br>'
       if enemyDict['hp'] <= 0:
           print enemy + ' has died'
           loser=enemy
           winner=userName
           break
       damage=(enemyDict['attack']+enemRandDam) - (0.5*userDict['defence'])
       if damage < 1:
           damage=1
       userDict['hp']=userDict['hp']-damage
       print userName +  ' was hit for ' + str(damage)+'<br>'
       print userName + ' has ' + str(userDict['hp']) + ' left '+'<br>'
       if userDict['hp'] <=0:
           print userName + ' has died'
           loser = userName
           winner = enemy
           break
    else:
        damage=(enemyDict['attack']+enemRandDam) - (0.5 * enemyDict['defence'])
        if damage < 1:
            damage=1
        userDict['hp']=userDict['hp']-damage
        print userName + ' was hit for ' + str(damage) + '<br>'
        print userName + ' has ' + str(userDict['hp']) + ' left' + '<br>'
        if userDict['hp'] <= 0:
            print userName + ' has died'
            loser = userName
            winner = enemy
            break
        damage=(userDict['attack']+enemRandDam) - (0.5*userDict['defence'])
        if damage < 1:
            damage = 1
        enemyDict['hp']=enemyDict['hp'] - damage
        print enemy + ' was hit for ' + str(damage) + '<br>'
        print enemy + ' has ' + str(enemyDict['hp']) + ' left' + '<br>'
        if enemyDict['hp'] <= 0:
            print enemy + ' has died'
            loser = enemy
            winner = userName
            break

moneyAddition=0
if winner == userName:
    moneyAddition=150 * enemyDict['level']
    originUserDict['level'] = str(float(originUserDict['level'])+1)
else:
    moneyAddition=(0-100) * enemyDict['level']

originUserDict['energy']=str(float(originUserDict['energy'])-20)
originUserDict['money']=str(float(originUserDict['money']) + moneyAddition)




  
writeString=originUserDict['lastLogin']+','+originUserDict['robohashLink']+',' + originUserDict['energy'] + ',' + originUserDict['speed'] + ',' + originUserDict['attack'] + ','+ originUserDict['defence'] + ',' + originUserDict['money'] + ',' + originUserDict['level'] + ',' + originUserDict['hp'] + '\n'




f=open('dirOfAccounts/a' + userName + '.txt','a')
f.write(writeString)
f.close
   

print '<br><h1>'
print 'winner: ' + winner
print '<br>loser: ' + loser
print '</h1>'
print '<form action="town.py" method="POST">'
print '<input type="hidden" name="ooser" value="' + userName + '">'
print '<input type="submit" name="submit" value="return to town">'
print '</form>'

print '</body></html>'
