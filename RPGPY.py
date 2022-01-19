import random
from time import sleep
print("Welcome to RPGPY")
playerhp = 200
bosshp = 200
while playerhp > 0 or bosshp > 0:
    print("What do you want to do?")
    action = input("")
    if (action =="Attack"):
        rand = random.randrange(1, 50)
        bosshp = bosshp - rand
        print(f"You did " + str(rand) + " damage, the boss is now at " + str(bosshp))
        rand = random.randrange(1, 50)
        playerhp = playerhp - rand
        print(f"The boss hits you! It does " + str(rand) + " damage, you are now at " + str(playerhp))
    elif (action =="Item"):
        rand2 = random.randrange(1, 20)
        playerhp = playerhp + rand2
        print(f"You are now at " + str(playerhp))
        rand = random.randrange(1, 50)
        playerhp = playerhp - rand
        print(f"The boss hits you! It does " + str(rand) + " damage, you are now at " + str(playerhp))
    else:
        print("Invalid Action")
    if playerhp < 1:
        print("Game over, you may close the script now, open it again to restart. Thanks for playing.")
        break
    if bosshp < 1:
        print("You win, you may close the script now, open it again to restart. Thanks for playing.")
        break
sleep(500)