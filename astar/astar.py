from queue import PriorityQueue
from Map import Map_Obj

def heuristic (pos1: list [int,int],pos2: list [int,int]) -> int:
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

# A* algorithm       (Reference: https://www.redblobgames.com/pathfinding/a-star/introduction.html)
def A_star (map:Map_Obj, start: list[int,int], goal: list[int,int]):
    """Main function to carry out search to find the path and cost

    Parameters
    ----------
    map : Map_Obj
        map for the task
    start : list[int, int]
        starting point
    goal : list[int, int]
        goal point

    Returns
    -------
    exploredPath : dict
        A dictionary of all explored postion with linking
    cost : int
    the cost from start to goal

    """
    exploredPos = PriorityQueue()       # priority queue for storing estimated of current frontier positions
    actualCost = {}                     # actual costs of the starting position to each reached position
    exploredPath = {}                   # dictionary for path

    exploredPos.put((0,start))
    actualCost[tuple(start)] = 0
    exploredPath[tuple(start)] = None

    while not exploredPos.empty():

        currentPos = exploredPos.get()[1]      # pop the least-cost position from queue
        
        if currentPos == goal:
            # reach the goal
            break
            
        neighbors = map.get_neighbors(currentPos)                                        # a list of the neighboring positions
        for next in neighbors:
            newActualCost = actualCost[tuple(currentPos)] +  map.get_cell_value(next)    # calculate acutal cost from start to next

            if tuple(next) not in actualCost or newActualCost < actualCost[tuple(next)]:
                actualCost[tuple(next)] = newActualCost                        # update actual cost dictionary
                estimatedCost = newActualCost + heuristic(goal,next)           # get new estimated cost from next
                exploredPos.put((estimatedCost,next))                            
                exploredPath[tuple(next)] = currentPos
                
    if tuple(goal) not in exploredPath:
        return None, None
    else:
        return exploredPath, actualCost[tuple(goal)]


def visualise_path (positionDict: dict, start: list[int,int], goal: list[int,int], map:Map_Obj) :
    """Calculate heuristic distance between two points

    Parameters
    ----------
    positionDict : dict
        dictionary of the points explored by A*
    start : list[int, int]
        start point
    goal : list[int, int]
        goal point
    map : Map_Obj
        map object

    Returns
    -------
    value : float
        heuristic distance
    """
    current = goal
    while current != start:
        current = positionDict[tuple(current)]  # trace back from goal
        if current != start:
            map.set_walked(current)  # set path as yellow


# task 1    
def task (taskNum:int):
    """
    Solution to any task with a task number 1-4.
    """
    # initialize task environment
    map = Map_Obj(task=taskNum)
    start = map.get_start_pos()
    goal = map.get_goal_pos()

    exploredPath,cost = A_star(map,start,goal)

    # generate path and visualise it, print the cost
    if exploredPath == None:
        return print("No path found")
    visualise_path(exploredPath,start,goal,map)
    print(f"Total cost of the path in task {taskNum} is: {cost}" )
    map.show_map()


# execute solution function for every task
for i in range(1,5):
    task(i)



