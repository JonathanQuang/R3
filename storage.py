#!/usr/bin/python

import cgitb
import gameLibFunctions
import cgi
cgitb.enable()

print '<!DOCTYPE html><html><head><title>Bits n Bolts</title></head><body>'

query = cgi.FieldStorage()
userName = query['ooser'].value
buttonThing = query['submit'].value

openString = 'dirOfAccounts/a' + userName + '.txt'
f = open(openString)
s = f.read()
f.close
gameLibFunctions.updateEnergy(openString)
pyDict = gameLibFunctions.getRecentDict(openString)

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
print '<table border="1"><tr><th>Weapon or Armor</th><th>+Attack</th><th>+Defense</th><th>+Speed</th><th>+Capacity</th><th>Description</th><th>Cost</th><th>Picture</th></tr>'
for storeItems in storeDict:
    print '<tr><td>' + storeDict[storeItems]['weaponOrArmor'] + '</td><td><form action = "store.py"><input type="hidden" name="ooser" value="' + userName + '"><input type="submit" name = "buyItem" value = "Buy Item"></form></td>'
    print '<td>' + storeDict[storeItems]['attPlus'] + '</td>'
    print '<td>' + storeDict[storeItems]['defPlus'] + '</td>'
    print '<td>' + storeDict[storeItems]['spdPlus'] + '</td>'
    print '<td>' + storeDict[storeItems]['description'] + '</td>'
    print '<td>' + storeDict[storeItems]['cost'] + '</td>'
    print '<td>' + storeDict[storeItems]['picture'] + '</td></tr>'
print '</table>'

if "buyItem" in query:
    buttonThing = query["buyItem"].value
if float(pyDict['money']) >= float(pyDict[buttonThing]['cost']):
    pyDict['attack'] = str(float(pyDict['attack']) + storeDict[buttonThing]['attPlus'])
    pyDict['defence'] = str(float(pyDict['defence']) + storeDict[buttonThing]['defPlus'])
    pyDict['speed'] = str(float(pyDict['speed']) + storeDict[buttonThing]['spdPlus'])
    pyDict['money'] = str(float(pyDict['money']) - storeDict[buttonThing]['cost'])
else:
    print "You do not have enough money to buy that item"

print '<form action="town.py" method="GET">'
print '<input type="hidden" name="ooser" value="' + userName + '">'
print '<input type="submit" name="submit" value="Head Back to Town">'
print '</form>'

print '</body></html>'

writeString = pyDict['lastLogin'] + ',' + pyDict['robohashLink'] + ',' + pyDict['energy'] + ',' + pyDict['speed'] + ',' + pyDict['attack'] + ',' + pyDict['defence'] + ',' + pyDict['money'] + ',' + pyDict['level'] + ',' + pyDict['hp'] + '\n'
f = open('dirOfAccounts/a' + userName + '.txt', 'a')
f.write(writeString)
f.close
