from queue import Queue
import copy
answer = []
def DFS(current, Limit): # Same for DLS, however
    result = battle(current)
    if answer != [] or Limit == 0:
        return
    if result == "Victory!":
        answer = current
        return
    elif result == "You Died. Restart?" or result == "Invalid command":
        return
    
    for acts in ["Attack", "Cure", "Fire", "Potion", "Defend"]:
        temp = copy.deepcopy(current)
        temp.append(acts)
        if acts == "Attack" or acts == "Fire":
            for target in ["wererat", "spritzer"]:
                temp2 = copy.deepcopy(temp)
                DFS(temp2, Limit - 1)
        else:
            temp.append("Y")
            DFS(temp, Limit - 1)

for i in range(0, 4): # We iterate through depth limit
    DFS([], 4)
    if answer != []:
        break