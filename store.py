#!/usr/bin/python
print 'content-type: text/html \n'


import cgitb
import gameLibFunctions
import cgi
cgitb.enable()

print '<!DOCTYPE html><html><head><title>Bits n Bolts</title></head><body style="background-color:#99ccff;">'



query = cgi.FieldStorage()
userName = query['ooser'].value
buttonThing = query['submit'].value



openString = 'dirOfAccounts/a' + userName + '.txt'
f = open(openString)
s = f.read()
f.close
gameLibFunctions.updateEnergy(openString)
pyDict = gameLibFunctions.getRecentDict(openString)

secOpen='secondaryDir/a' + userName + '.txt'
f=open(secOpen)
secondS=f.read()
f.close()

secondS=secondS.strip()
secondS=secondS.split('\n')
lastLine=secondS[len(secondS)-1]
lastLine=lastLine.split(',')
storedItems=lastLine[1]
storedItems=storedItems.split(':')



g = open('items.txt')
storeStuff = g.read()
g.close

storeStuff = storeStuff.strip()
storeStuff = storeStuff.split('\n')
titles = storeStuff[0].split(',')
store = storeStuff[1:]

storeDict = {}

for items in store:
    items = items.split(',')
    count = 0
    for data in items:
        if data == items[0]:
            storeDict[data] = {}
        else:
            storeDict[items[0]][titles[count]] = data
        count += 1

print '<img src="' + pyDict['robohashLink']+ '">'
print '<table border="1"><tr><th>Battery Life</th><td>' + pyDict['energy'] + '</td></tr>'
print '<tr><th>AttackPwr</th><td>' + pyDict['attack'] + '</td></tr>'
print '<tr><th>Force Field Capacity</th><td>' + pyDict['defence'] + '</td></tr>'
print '<tr><th>Speed</th><td>' + pyDict['speed'] + '</td></tr>'
print '<tr><th>Bolts</th><td>' + pyDict['money'] + '</td></tr>'
print '<tr><th>Level</th><td>' + pyDict['level'] + '</td></tr>'
print '<tr><th>Armor/HP</th><td>' + pyDict['hp'] + '</td></tr>'
print '</table>'
print '<br>'

print '<h1>Welcome to the Store</h1>'
print '<table border="1"><tr><th>Weapon or Armor</th><th>Buy it?</th><th>+Attack</th><th>+Defence</th><th>+Speed</th><th>Description</th><th>Cost</th><th>Picture</th></tr>'

print '<h3>The transactions you have made in the past are listed below in chrnological order:</h3></br>'
print 'note that the most recent item you have bought has not been processed yet<br>'

totalAttack=0
totalDefence=0
totalSpeed=0

for x in storedItems:
    if x in storeDict:
        print x + '<br>'
        totalAttack += float(storeDict[x]['attPlus'])
        totalDefence += float(storeDict[x]['defPlus'])
        totalSpeed += float(storeDict[x]['spdPlus'])
print 'The total buffs provided by these items are:<br>'
print '+' + str(totalAttack) + ' attack' + '<br>'
print '+' + str(totalDefence) + ' defence' + '<br>'
print '+' + str(totalSpeed) + ' speed<br>'

for storeItems in storeDict:
    print '<tr><td>' + storeItems + '</td><td><form action = "store.py" method="POST"><input type="hidden" name="ooser" value="' + userName + '"><input type="submit" name = "submit" value ="' + storeItems + '"></form></td>'
    print '<td>' + storeDict[storeItems]['attPlus'] + '</td>'
    print '<td>' + storeDict[storeItems]['defPlus'] + '</td>'
    print '<td>' + storeDict[storeItems]['spdPlus'] + '</td>'
    print '<td>' + storeDict[storeItems]['description'] + '</td>'
    print '<td>' + storeDict[storeItems]['cost'] + '</td>'
    print '<td>' + '<img src="' + storeDict[storeItems]['picture'] + '" style="height:100px;"></td></tr>'
print '</table>'




if not(buttonThing=='Head to the store'):
    
    if float(pyDict['money']) >= float(storeDict[buttonThing]['cost']):
        pyDict['attack'] = str(float(pyDict['attack']) + float(storeDict[buttonThing]['attPlus']))
        pyDict['defence'] = str(float(pyDict['defence']) + float(storeDict[buttonThing]['defPlus']))
        pyDict['speed'] = str(float(pyDict['speed']) + float(storeDict[buttonThing]['spdPlus']))
        pyDict['money'] = str(float(pyDict['money']) - float(storeDict[buttonThing]['cost']))
        f=open(secOpen,'a')
        f.write(lastLine[0] + ',' + lastLine[1] + ':' + buttonThing + '\n')
        f.close()
    else:
        print "You do not have enough money to buy " + buttonThing

print '<form action="town.py" method="GET">'
print '<input type="hidden" name="ooser" value="' + userName + '">'
print '<input type="submit" name="submit" value="Head Back to Town">'
print '</form>'

print '</body></html>'

writeString = pyDict['lastLogin'] + ',' + pyDict['robohashLink'] + ',' + pyDict['energy'] + ',' + pyDict['speed'] + ',' + pyDict['attack'] + ',' + pyDict['defence'] + ',' + pyDict['money'] + ',' + pyDict['level'] + ',' + pyDict['hp'] + '\n'
f = open('dirOfAccounts/a' + userName + '.txt', 'a')
f.write(writeString)
f.close




