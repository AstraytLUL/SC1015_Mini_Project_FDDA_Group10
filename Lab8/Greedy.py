import copy
answer = [] # Storing answer we found

def cost(player, enemies, bag): # Cost Function = max(E1 HP, E2 HP) + 10^18 * WillDie - 1000 * Potion
    dmg = 0
    enemy1 = enemies.enemy1
    enemy2 = enemies.enemy2
    WillDie = 0
    
    # Check if we will die from enemy attack if they all hit
    if enemy1.state == 1:
        dmg += int(phy_dmg_reduced(phy_dmg(enemy1.attack, enemy1.strength), player.defense))
    if enemy2.state == 1:
        dmg += int(phy_dmg_reduced(phy_dmg(enemy2.attack, enemy2.strength), player.defense))
    if dmg >= player.HP:
        WillDie = 1
        
    return max(enemy1.HP, enemy2.HP) + 10**18 * WillDie - 1000 * bag.potion


def Greedy():
    actions = [] # Initial Sequence
    while answer == []: # Start of Greedy
        if answer != []:
            break
        CurCost = 2 * 10 ** 18
        next = []
        for acts in ["Attack", "Cure", "Fire", "Potion", "Defend"]: # Go through every possible next action
            temp = copy.deepcopy(actions) 
            temp.append(acts)
            if acts == "Attack" or acts == "Fire":
                for target in ["wererat", "spritzer"]: # Selecting target
                    temp2 = copy.deepcopy(temp) 
                    temp2.append(target)
                    player, enemies, bag, result = battle(temp2) # Get info for calculating cost
                    if result == "Victory!": # If won, we found the answer, no more greedy required
                        answer = temp2
                        break
                    elif result == "You Died. Restart?" or result == "Invalid command":
                        continue # Eliminate impossible sequences
                    if CurCost > cost(player, enemies, bag): # If the cost is lower, then we will consider this as our best choice
                        CurCost = cost(player, enemies, bag)
                        next = temp2
                        
                        
                        
            else:
                temp.append("Y")
                player, enemies, bag, result = battle(temp) # Get info for calculating cost
                if result == "Victory!": # If won, we found the answer, no more greedy required
                    answer = temp
                    break
                elif result == "You Died. Restart?" or result == "Invalid command":
                    continue # Eliminate impossible sequences
                if CurCost > cost(player, enemies, bag): # If the cost is lower, then we will consider this as our best choice
                    CurCost = cost(player, enemies, bag)
                    next = temp
        actions = next # Move on to search for the next move
                
Greedy()