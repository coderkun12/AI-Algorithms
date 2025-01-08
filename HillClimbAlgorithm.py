import random
import copy

class Puzzle8:
    def __init__(self, initial_state):
        self.goal_state = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
        self.state = initial_state

    def print_state(self):
        for row in self.state:
            print(row)
        print()

    def get_blank_position(self):
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    return i, j

    def get_successors(self):
        successors = []
        blank_i, blank_j = self.get_blank_position()
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]  
        for move in moves:
            new_i, new_j = blank_i + move[0], blank_j + move[1]
            if 0 <= new_i < 3 and 0 <= new_j < 3:
                new_state = copy.deepcopy(self.state)
                new_state[blank_i][blank_j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[blank_i][blank_j]
                successors.append(new_state)
        return successors

    def heuristic(self):
        count = 0
        for i in range(3):
            for j in range(3):
                if self.state[i][j] != self.goal_state[i][j]:
                    count += 1
        return count

    def solve_hill_climbing(self):
        current_state = self.state
        current_heuristic = self.heuristic()
        visited_states = set()
        while True:
            print("Current state:")
            self.print_state()
            successors = self.get_successors()
            print("Successors:")
            for s in successors:
                print(s)
            best_successor = None
            best_heuristic = float('inf')
            for successor in successors:
                successor_puzzle = Puzzle8(successor)
                successor_heuristic = successor_puzzle.heuristic()
                if successor_heuristic < best_heuristic and tuple(map(tuple, successor)) not in visited_states:
                    best_successor = successor
                    best_heuristic = successor_heuristic
            if best_heuristic >= current_heuristic:
                break
            current_state = best_successor
            current_heuristic = best_heuristic
            visited_states.add(tuple(map(tuple, current_state)))
        return current_state

if __name__ == "__main__":
    initial_state = [[2, 8, 3], [1, 6, 4], [7, 0, 5]]
    puzzle = Puzzle8(initial_state)
    print("Initial State:")
    puzzle.print_state()
    solution = puzzle.solve_hill_climbing()
    print("Solution:")
    puzzle.print_state()
