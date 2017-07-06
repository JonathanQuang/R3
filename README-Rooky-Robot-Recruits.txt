=====================================================================================
=========R3: Rooky Robot Recruits=========By: Herman Lin and Jonathan Quang==========
=====================================================================================
*yes rooky is an actual word


===========================
=========Summary:==========
===========================
Project created by Jonathan Quang and Herman Lin for Dyrland-Weaver's Period 2 IntroCS2 class
For our project Rooky Robot Recruits (R3), we decided to make an RPG that is sort of a PG 
friendly parody of Alienaa.com (a.k.a A3)
We have created a rudimentary login and register system. After logging in, the player is 
presented with most of their current stats. They can head to town where they will find 
multiple things to do.
These actions require energy/battery to do
Energy is replenished the next day the player logs in thanks to the python time library
You can also purchase items that increase your stats. 
The overall goal of this game is to become the dictator by having the highest level, which 
requires winning a lot of battles, which in turn requires raising stats and getting money

The URL at which this project is hosted is homer.stuy.edu/~jonathan.quang/project/account.html

===============================
==========How to play:=========
===============================


-=-=-=-Registering-=-=-=-
Register an account to start playing.
Once you have created an account, head back to the login screen and login into your newly 
created account to begin your adventure.
You will be sent to a verification page once logged in.

**************************************************************************************************
*NOTE*: We have provided you with an account with large amounts of energy and money hacked into it
 to play around with to avoid the issue of waiting a day for energy to replenishe
 The username is MrDW and the password is dw2
**************************************************************************************************

-=-=-=-Starting Page-=-=-=-
The starting page shows you your randomly generated robot provided by robohash.org and stats below it:
Battery Life - how much energy you have to perform tasks
AttackPwr - how much attack damage you have
Force Field Capacity - how much defense you have
Speed - how fast your robot is
Bolts - Rooky Robot Recruits's in-game currency
Level - what level your robot is 
Armor/HP - how much health points your robot has
Intelligence - how smart your robot is
Click "head to town" to head to town
Click "Logout" under the "head to town" button to log out of your account

-=-=-=-Town-=-=-=-
The Town page displays a couple of things:
Your robot and the battery life and how many Bolts you have
The leaderboard at the bottom right
Buttons that lead to different areas within Robotville

-=-=-=-Arena-=-=-=-
In the arena, you can battle it out against other players around your level (+/- 4 levels)
You need to have at least 20 Battery Life if you want to participate in the arena

Once you have chosen your opponent and clicked the "fight" button, you'll be brought to a
simple battle page. The battle is a log of who did what damage. Attack determines how much damage is done,
defence/forcefield capacity is how much the damage is reduced, and speed determines who 
goes first as well as the max random damage they do during a random damage calculation

-=-=-=-Gym-=-=-=-
The Gym is where you can upgrade stats on your robot to have better chances fighting other robots
It requires 20 Bolts and 5 Battery Life in order to train one stats

You can train 4 different stats on your robot here:
Upgrade Torque for increased AttackPwr
Upgrade Capacitor for increased Force Field Capacity
Get New Rims for increased Speed
Get more armour for increased hp

-=-=-=-School-=-=-=-
Attend school to increase your robot's intelligence. Increased intelligence can get you better
jobs when attending work. Going to school requires 50 Battery Life

-=-=-=-Work-=-=-=-
Going to work helps gain Bolts so you can perform other tasks that require currency
Working requires at least 25 Battery Life
Gain intelligence by going to school in order to have better paying jobs

-=-=-=-Store-=-=-=-	
The Store is where you can go to obtain weapons or defence items
Certain items increase or decrease your attack, defence, or speed for certain prices
Buy items if you want to have better chances at surviving the arena


-=-=-=-Bugs-=-=-=-
The leader board in town.py is subject to weirdness that comes with the os.listdir function, so when ties in level occurs,
the leader board will not update as expected.
Any python files that have buttons that lead to the same page (such as the gym page or the store page) show player information
that has not been updated yet.
During bugtesting with friends, negative battery has been found to occur, but we can't seem to locate where it happens.
Sometimes form data goes missing, and we have yet to trace that down. We can repeat the same actions, but only sometimes do they result in a crash
that is related to missing form data.
