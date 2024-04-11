from queue import Queue
import copy
answer = []
def DFS(current, Limit): # Almost same for DFS, however
    result = battle(current)
    if answer != [] or Limit == 0: # We added a search depth limit here
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
            
DFS([], 4)