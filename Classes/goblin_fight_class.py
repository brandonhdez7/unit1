
import os 
#from [NAMEOFFILE] import [CLASS] 
from Hero import Hero 
from Goblin import Goblin 

hero_name = raw_input("What is your name, brave hero? ")
theHero = Hero(hero_name, 8)
theHero.cheer_hero()

goblin = Goblin()

while(1):
       print """You have %d health and %d power.
        The goblin has %d health and %d power. 
        What do you want to do?
        1. Fight goblin
        2. Dance!
        3. Flee
        > """ % (theHero.health, theHero.power, goblin.health, goblin.power)
        
        user_input = raw_input("> ")

        if user_input == "1":     
            goblin.take_damage(theHero.power)
            print "You have done %d damage to the goblin" % theHero.power
        elif user_input == "2":
            goblin.power += 5
            print """You embarrassed yourself!
            You also increased the goblin's health!
            SAD!"""
            print "Your health is now %d" % theHero.health
        elif user_input == "3":
            print "Goodbye, %s, you shameful creature!" % hero_name
        else: 
            print "You have stumbled. Try to follow the instruction next time.."
        if goblin.health > 0: 
            theHero.health -= goblin.power
            print "The goblin hits you for %d damage" % goblin.power
            if theHero.health <= 0:
                print """Thou hast been slain. 
                Prepare to meet your unmaker
                            ,-.                               
       ___,---.__          /'|`\          __,---,___          
    ,-'    \`    `-.____,-'  |  `-.____,-'    //    `-.       
  ,'        |           ~'\     /`~           |        `.      
 /      ___//              `. ,'          ,  , \___      \    
|    ,-'   `-.__   _         |        ,    __,-'   `-.    |    
|   /          /\_  `   .    |    ,      _/\          \   |   
\  |           \ \`-.___ \   |   / ___,-'/ /           |  /  
 \  \           | `._   `\\  |  //'   _,' |           /  /      
  `-.\         /'  _ `---'' , . ``---' _  `\         /,-'     
     ``       /     \    ,='/ \`=.    /     \       ''          
             |__   /|\_,--.,-.--,--._/|\   __|                  
             /  `./  \\`\ |  |  | /,//' \,'  \                  
            /   /     ||--+--|--+-/-|     \   \                 
           |   |     /'\_\_\ | /_/_/`\     |   |                
            \   \__, \_     `~'     _/ .__/   /            
             `-._,-'   `-._______,-'   `-._,-')"""
        
        #clean up game space after each turn 
        raw_input("Hit enter to continue")
        os.system("clear")