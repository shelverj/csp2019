import random
#was very confused
#got some assistance from existing rpsls programs although
#i tried to make this one unique and more user-friendly
def a(num):
    #converts number to name
    if num == 0:
        result = "rock"
    elif num == 1:
        result = "Spock"
    elif num == 2:
        result = "paper"
    elif num == 3:
        result = "lizard"
    elif num == 4:
        result = "scissors"
    return result 
    
def b(name):
   #converts name to number
    if name == "rock":
        result = 0
    elif name == "Spock":
        result = 1
    elif name == "paper":
        result = 2
    elif name == "lizard":
        result = 3
    elif name == "scissors":
        result = 4
    return result

def rpsls(name): 
   #see if players pick beats computers randomly generated pick
    player_number = b(name)
    comp_number = random.randrange(0, 5)
   
    print "You picked", name
    print "Computer picked", a(comp_number)
   
    if (comp_number + 1) % 5 == player_number:
        print "Player wins!"
    elif (comp_number + 2) % 5 == player_number:
        print "Player wins!"
    elif comp_number == player_number:
        print "Player and computer tie!"
    else:
        print "Computer wins!"
    print ""    

print """- Welcome to rock paper scissors lizard spock!
It's just like rock paper scissors except there are two
more moves to make it more confusing. Spock beats rock and
scissors and loses to paper and lizard, while lizard beats
spock and paper and loses to rock and scissors. Ready?"""
print "- type ro, pa, sc, li, or sp and press enter"
#user input
answer = raw_input()
if answer == "ro":
    rpsls("rock")
elif answer == "pa":
    rpsls("paper")
elif answer == "sc":
    rpsls("scissors")
elif answer == "li":
    rpsls("lizard")
elif answer == "sp":
    rpsls("Spock")
else:
    print "bad" 
     