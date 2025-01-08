from queue import PriorityQueue

# Define State class to represent the state of the robot
class State:
    def __init__(self, x, y, parent=None):
        self.x = x  # x-coordinate
        self.y = y  # y-coordinate
        self.parent = parent  # parent state

# Define the heuristic function (Euclidean distance)
def euclidean_distance(state, goal_state):
    return ((state.x - goal_state.x) ** 2 + (state.y - goal_state.y) ** 2) ** 0.5

# Generate successor states for the given state
def generate_successor_states(state, grid):
    successors = []
    movements = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # Right, Down, Left, Up

    for dx, dy in movements:
        new_x, new_y = state.x + dx, state.y + dy
        if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] != 1:
            successors.append(State(new_x, new_y, state))

    return successors

# Best-First Search algorithm
def best_first_search(initial_state, goal_state, heuristic_func):
    priority_queue = PriorityQueue()
    priority_queue.put((heuristic_func(initial_state, goal_state), initial_state))
    visited = set()

    while not priority_queue.empty():
        _, current_state = priority_queue.get()

        if current_state == goal_state:
            return reconstruct_path(current_state)

        visited.add(current_state)

        for successor_state in generate_successor_states(current_state, grid):
            if successor_state not in visited:
                priority_queue.put((heuristic_func(successor_state, goal_state), successor_state))

    return None  # Failure

# Reconstruct the path from the goal state to the initial state
def reconstruct_path(state):
    path = [state]
    while state.parent:
        path.append(state.parent)
        state = state.parent
    return path[::-1]

# Example grid representing the environment (0: free space, 1: obstacle)
grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0]
]

# Define initial state and goal state
initial_state = State(0, 0)
goal_state = State(4, 4)

# Call the Best-First Search algorithm
path = best_first_search(initial_state, goal_state, euclidean_distance)

if path:
    print("Path found:")
    for state in path:
        print(f"({state.x}, {state.y}) -> ", end="")
    print("Goal")
else:
    print("No path found")
