from queue import PriorityQueue

class PuzzleState:
    def __init__(self, puzzle, parent=None, action=None, depth=0):
        self.puzzle = puzzle
        self.parent = parent
        self.action = action
        self.depth = depth
        self.cost = self.calculate_cost()

    def __lt__(self, other):
        return self.cost < other.cost

    def calculate_cost(self):
        # Heuristic function: Manhattan distance
        goal_state = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        cost = 0
        for i in range(3):
            for j in range(3):
                if self.puzzle[i][j] != 0:
                    row, col = divmod(self.puzzle[i][j] - 1, 3)
                    cost += abs(row - i) + abs(col - j)
        return cost + self.depth

    def get_blank_position(self):
        for i in range(3):
            for j in range(3):
                if self.puzzle[i][j] == 0:
                    return i, j

    def get_next_states(self):
        blank_row, blank_col = self.get_blank_position()
        next_states = []
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for move in moves:
            new_row, new_col = blank_row + move[0], blank_col + move[1]
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_puzzle = [row[:] for row in self.puzzle]
                new_puzzle[blank_row][blank_col] = new_puzzle[new_row][new_col]
                new_puzzle[new_row][new_col] = 0
                next_states.append(PuzzleState(new_puzzle, self, move, self.depth + 1))
        return next_states

    def is_goal_state(self):
        return self.puzzle == [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

    def get_solution_path(self):
        path = []
        current_state = self
        while current_state:
            path.append((current_state.action, current_state.puzzle))
            current_state = current_state.parent
        path.reverse()
        return path

def best_first_search(initial_state):
    OPEN = PriorityQueue()
    CLOSED = set()

    OPEN.put(initial_state)
    while not OPEN.empty():
        current_state = OPEN.get()
        CLOSED.add(tuple(map(tuple, current_state.puzzle)))

        if current_state.is_goal_state():
            return current_state.get_solution_path()

        for next_state in current_state.get_next_states():
            if tuple(map(tuple, next_state.puzzle)) not in CLOSED:
                OPEN.put(next_state)

    return None

def print_solution_path(path):
    print("Solution path:")
    for action, puzzle in path:
        print(f"Action: {action if action else 'Start'}, Puzzle:")
        for row in puzzle:
            print(row)
        print()

if __name__ == "__main__":
    initial_puzzle = [
        [1, 2, 3],
        [4, 0, 6],
        [7, 5, 8]
    ]
    initial_state = PuzzleState(initial_puzzle)
    solution_path = best_first_search(initial_state)
    if solution_path:
        print_solution_path(solution_path)
    else:
        print("No solution found.")
