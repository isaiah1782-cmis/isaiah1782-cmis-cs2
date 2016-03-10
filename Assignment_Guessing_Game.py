import math
import random
YourName = raw_input("What is your name?: ")
enemy1 = raw_input("What do you want to name your first enemy?: ")
enemy2 = raw_input("What do you want to name your second enemy?: ")
def eat(item):

    if item == "nothing":
        strength = 0    
    elif item == "money":
        strength = 1
    elif item == "bugs":
        strength = 1
    elif item == "deez nuts":
        strength = 2
    elif item == "duck":
        strength = 3
    elif item == "bear liver":
        strength = 4
    elif item == "fried rice":
        strength = 5
    elif item == "toe nails":
        strength = 6
    elif item == "finger nails":
        strength = 7
    elif item == "Graeme":
        strength = 8
    elif item == "slippery snakes":
        strength = 9
    elif item == "Pizza":
        strength = 10
    elif item == "Calzone":
        strength = 11
    elif item == "Hamburger":
        strength = 12
    elif item == "drugs":
        strength = 999999
    elif item == "Bryson's Seceret Sauce":
        strength = 9999999
    else:
        strength = random.randint(0,10)
    return strength * random.random()

def getAttackValue():
 
    number = int(raw_input("Type attack value (0-99): "))
    if number > 99 or number < 0:
        number = random.randint(0, 99)
    attackValue = float(number)/100
    return attackValue


def wrestle(playerStrength, enemyStrength, playerAttackValue):

    targetValue = random.random()
    playerAttackResult = playerStrength + abs(playerAttackValue - targetValue)    
    enemyAttackResult =  enemyStrength + targetValue
    if playerAttackResult > enemyAttackResult:
        return True
    else:
        return False


def resultTemplate(playerStrength, enemyStrength, result):

    if result == True:
        msg = "wins"
    else:
        msg = "loses"
    return """
Player strength: {}
Enemy strength: {}
Player {}!
""".format(playerStrength, enemyStrength, msg)

def main():


    playerFood = raw_input("What do you want to eat? ")
    enemy1Food = raw_input("What does " + enemy1 + " eat? ")
    enemy2Food = raw_input("What does " + enemy2 + " eat? ")

    playerStrength = eat(playerFood)
    enemy1Strength = eat(enemy1Food)
    enemy2Strength = eat(enemy2Food)

    playerAttackValue1 = getAttackValue()
    result1 = wrestle(playerStrength, enemy1Strength, playerAttackValue1)

    playerAttackValue2 = getAttackValue()   
    result2 = wrestle(playerStrength, enemy2Strength, playerAttackValue2)
    
    output = """
""" + YourName + """ ate {}.
""" + enemy1 + """ ate {}.
""" + enemy2 + """ ate {}.
""".format(playerFood, enemy1Food, enemy2Food)
    output += resultTemplate(playerStrength, enemy1Strength, result1)
    output += resultTemplate(playerStrength, enemy2Strength, result2)

    print output

main()
