#!/usr/bin/python
print 'content-type: text/html\n'
import cgitb
import gameLibFunctions
import random
import cgi
cgitb.enable()

print '<!DOCTYPE html><html><head><title>The Mechanic</title></head><body background="http://thumbs.dreamstime.com/t/illustration-weights-fitness-cartoon-36813258.jpg">' 


query = cgi.FieldStorage()


userName = query['ooser'].value



statString = 'dirOfAccounts/a' + userName + '.txt'
f = open(statString)
s = f.read()
f.close




gameLibFunctions.updateEnergy(statString)
pyDict = gameLibFunctions.getRecentDict(statString)




print '<img src="' + pyDict['robohashLink']+ '">'
print '<table border="1" bgcolor="white"><tr><th>Battery Life</th><td>' + pyDict['energy'] + '</td></tr>'
print '<tr><th>AttackPwr</th><td>' + pyDict['attack'] + '</td></tr>'
print '<tr><th>Force Field Capacity</th><td>' + pyDict['defence'] + '</td></tr>'
print '<tr><th>Speed</th><td>' + pyDict['speed'] + '</td></tr>'
print '<tr><th>Bolts</th><td>' + pyDict['money'] + '</td></tr>'
print '<tr><th>Level</th><td>' + pyDict['level'] + '</td></tr>'
print '<tr><th>Armor/HP</th><td>' + pyDict['hp'] + '</td></tr>'
print '</table>'


print '<form action="planetfitness.py" method="POST">'
print '<input type="hidden" name="ooser" value="' + userName + '">'
print '<input type="submit" name="attackPlus" value="Upgrade torque (+AttackPwr)">'
print '<br>'
print '<input type="submit" name="defensePlus" value="Upgrade Capacitor (+Force Field Capacity)">'
print '<br>'
print '<input type="submit" name="speedPlus" value="Get New Rims (+Speed)">'
print '<br>'
print '<input type="submit" name="armorPlus" value="Get more Armor (+hp)">'
print '</form>'



if float(pyDict['money']) > 20:
    if float(pyDict['energy']) > 5:
        if "attackPlus" in query:
            pyDict['attack'] = str(float(pyDict['attack']) + random.randrange(1, 5))
            pyDict['money'] = str(float(pyDict['money']) - 20)
            pyDict['energy'] = str(float(pyDict['energy']) - 5)
            
        if "defensePlus" in query:
            pyDict['defence'] = str(float(pyDict['defence']) + random.randrange(1, 5))
            pyDict['money'] = str(float(pyDict['money']) - 20)
            pyDict['energy'] = str(float(pyDict['energy']) - 5)
            
            
        if "speedPlus" in query:
            pyDict['speed'] = str(float(pyDict['speed']) + random.randrange(1, 5))
            pyDict['money'] = str(float(pyDict['money']) - 20)
            pyDict['energy'] = str(float(pyDict['energy']) - 5)
        if "armorPlus" in query:
            pyDict['hp'] = str(float(pyDict['hp']) + random.randrange(1,5))
            pyDict['money']=str(float(pyDict['money']) - 20)
            pyDict['energy'] = str(float(pyDict['energy'])-5)

            
    else:
        print 'You do not have enough energy'
else:
    print 'You do not have enough money'



    
print '<form action="town.py" method="POST">'
print '<input type="hidden" name="ooser" value="' + userName + '">'
print '<input type="submit" name="submit" value="Head Back to Town">'
print '</form>'


                                  
print '</body></html>'

writeString = pyDict['lastLogin'] + ',' + pyDict['robohashLink'] + ',' + pyDict['energy'] + ',' + pyDict['speed'] + ',' + pyDict['attack'] + ',' + pyDict['defence'] + ',' + pyDict['money'] + ',' + pyDict['level'] + ',' + pyDict['hp'] + '\n'
f = open('dirOfAccounts/a' + userName + '.txt', 'a')
f.write(writeString)
f.close


