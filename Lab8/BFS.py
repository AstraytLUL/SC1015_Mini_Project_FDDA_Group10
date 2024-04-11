from queue import Queue
import copy
answer = [] # Storing answer we found
def BFS():
    actions = [] # Initial Sequence
    q = Queue() # Initializing of BFS
    q.put(actions)
    while q.empty == 0: # Start of BFS
        current = q.get()
        result = battle(current) # Get the result of current sequence
        if result == "Victory!": # If won, we found the answer, no more BFS required
            answer = current
            break
        elif result == "You Died. Restart?" or result == "Invalid command":
            continue # Eliminate impossible sequences
        for acts in ["Attack", "Cure", "Fire", "Potion", "Defend"]: # Go through every possible next action
            temp = copy.deepcopy(current) 
            temp.append(acts)
            if acts == "Attack" or acts == "Fire":
                for target in ["wererat", "spritzer"]: # Selecting target
                    temp2 = copy.deepcopy(temp) 
                    temp2.append(target)
                    q.put(temp2) # Enqueue the sequence for search
            else:
                temp.append("Y")
                q.put(temp) # Enqueue the sequence for search
                
BFS()