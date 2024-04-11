from queue import PriorityQueue
import copy
answer = [] # Storing answer we found

def cost(player, enemies, bag): # Cost Function
    enemy1 = enemies.enemy1
    enemy2 = enemies.enemy2
    return (max(enemy1.HP, 0) + max(enemy1.HP, 0)) * ((enemy1.state + enemy2.state)**3) - player.state * (player.HP + 10 * player.MP + 50 * bag.potion)


def UCS():
    cost = 0
    actions = [] # Initial Sequence
    q = PriorityQueue() # Initializing of UCS
    player, enemies, bag, result = battle(current)
    q.put((cost(player, enemies, bag), actions))
    while q.empty == 0: # Start of UCS
        current = q.get()
        if answer != []:
            break
        for acts in ["Attack", "Cure", "Fire", "Potion", "Defend"]: # Go through every possible next action
            temp = copy.deepcopy(current) 
            temp.append(acts)
            if acts == "Attack" or acts == "Fire":
                for target in ["wererat", "spritzer"]: # Selecting target
                    temp2 = copy.deepcopy(temp) 
                    temp2.append(target)
                    player, enemies, bag, result = battle(temp2) # Get info for calculating cost
                    if result == "Victory!": # If won, we found the answer, no more UCS required
                        answer = temp2
                        break
                    elif result == "You Died. Restart?" or result == "Invalid command":
                        continue # Eliminate impossible sequences
                    q.put((cost(player, enemies, bag), temp2)) # Put the tuple (cost, sequence) into priority queue
            else:
                temp.append("Y")
                player, enemies, bag, result = battle(temp) # Get info for calculating cost
                if result == "Victory!": # If won, we found the answer, no more UCS required
                    answer = temp
                    break
                elif result == "You Died. Restart?" or result == "Invalid command":
                    continue # Eliminate impossible sequences
                q.put((cost(player, enemies, bag), temp)) # Put the tuple (cost, sequence) into priority queue
                
UCS()