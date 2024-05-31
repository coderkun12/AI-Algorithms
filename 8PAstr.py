from queue import PriorityQueue
import copy

OPEN = PriorityQueue()
CLOSE = set()  

def heuristic_Val(cur, gol):
    val = 0
    for i in range(3):
        for j in range(3):
            if cur[i][j] != gol[i][j]:
                val += 1
    return val

def manhattan_distance(cur, gol):
    distance = 0
    for i in range(3):
        for j in range(3):
            if cur[i][j] != 0:
                row = (cur[i][j] - 1) // 3
                col = (cur[i][j] - 1) % 3
                distance += abs(row - i) + abs(col - j)
    return distance

def move(cur, i, j, new_i, new_j):
    cur[new_i][new_j], cur[i][j] = cur[i][j], cur[new_i][new_j]

def get_neighbors(cur):
    neighbors = []
    for i in range(3):
        for j in range(3):
            if cur[i][j] == 0:
                for new_i, new_j in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if 0 <= new_i < 3 and 0 <= new_j < 3:
                        neighbor = copy.deepcopy(cur)
                        move(neighbor, i, j, new_i, new_j)
                        neighbors.append(neighbor)
    return neighbors

def AStar(initial, final):
    OPEN.put((0, initial))
    flag = False

    while not OPEN.empty() and not flag:
        _, v = OPEN.get()
        
        CLOSE.add(tuple(map(tuple, v))) 
        if v == final:
            flag = True
            print('Reached Final Goal state:\t',v)
            break
        for neighbor in get_neighbors(v):
            if tuple(map(tuple, neighbor)) not in CLOSE:
                cost = manhattan_distance(neighbor, final)
                OPEN.put((cost, neighbor))

initial_puzzle = [[1, 2, 3], [4, 0, 6], [7, 5, 8]]
print("Initial goal state is as follow:\t",initial_puzzle)
goal_state = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
AStar(initial_puzzle, goal_state)