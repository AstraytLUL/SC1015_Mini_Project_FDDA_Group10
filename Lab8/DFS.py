from queue import Queue
import copy
answer = []
def DFS(current): # A recursive function for DFS
    result = battle(current) # Get the result of current sequence
    if answer != []: # If we have the answer, there is no more need to search
        return
    if result == "Victory!": # Same here
        answer = current
        return
    elif result == "You Died. Restart?" or result == "Invalid command":
        return # Eliminate impossible sequences
    
    for acts in ["Attack", "Cure", "Fire", "Potion", "Defend"]: # Go through every possible next actions
        temp = copy.deepcopy(current)
        temp.append(acts)
        if acts == "Attack" or acts == "Fire":
            for target in ["wererat", "spritzer"]:
                temp2 = copy.deepcopy(temp)
                DFS(temp2) # Go deeper into DFS
        else:
            temp.append("Y")
            DFS(temp) # Go deeper into DFS
            
DFS([])