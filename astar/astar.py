from queue import PriorityQueue
from Map import Map_Obj

def heuristic (pos1: list [int,int],pos2: list [int,int]) -> float:
    """Calculate heuristic distance between two points

    Parameters
    ----------
    pos1 : list[int, int]
        starting point
    pos2 : list[int, int]
        ending point

    Returns
    -------
    value : float
        heuristic distance
    """
    return abs(pos1[0]-pos2[0]) + abs (pos1[1]-pos2[1])


# task 1    (Reference: https://www.redblobgames.com/pathfinding/a-star/introduction.html)

def task1 ():
    """
    Solution to task 1.
    """
    # initialize task environment
    map = Map_Obj(task=3)
    start = map.get_start_pos()
    goal = map.get_goal_pos()
    exploredPos = PriorityQueue()       # priority queue for storing estimated of current frontier positions
    actualCost = {}                     # actual costs of the starting position to each reached position
    exploredPath = {}                   # dictionary for path

    exploredPos.put(start,0)
    actualCost[tuple(start)] = 0
    exploredPath[tuple(start)] = None

    while not exploredPos.empty():

        currentPos = exploredPos.get()
        
        
        if currentPos == goal:
            # reach the goal
            break
            
        neighbors = map.get_neighbors(currentPos)                                        # a list of the neighboring positions
        for next in neighbors:
            newActualCost = actualCost[tuple(currentPos)] +  map.get_cell_value(next)    # calculate acutal cost from start to next

            if tuple(next) not in actualCost or newActualCost < actualCost[tuple(next)]:
                actualCost[tuple(next)] = newActualCost                            # update actual cost dictionary
                estimatedCost = newActualCost + heuristic(goal,next)               # get new estimated cost from next
                exploredPos.put(next,estimatedCost)
                exploredPath[tuple(next)] = currentPos
    

    # generate path
    path=[]
    if tuple(goal) not in exploredPath:
        return print("No path found")
    current = goal
    while current != start:
        path.append(current)
        current = exploredPath[tuple(current)]
        if current != start:
            map.set_walked(current)


    
    map.show_map()



    


    

    

task1()




