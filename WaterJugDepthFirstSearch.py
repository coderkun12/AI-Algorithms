class WaterJugProblem:
    def __init__(self, jug1_capacity, jug2_capacity, target):
        self.jug1_capacity = jug1_capacity
        self.jug2_capacity = jug2_capacity
        self.target = target
        self.visited_states = set()

    def is_valid_state(self, state):
        jug1, jug2 = state
        return 0 <= jug1 <= self.jug1_capacity and 0 <= jug2 <= self.jug2_capacity

    def dfs(self, current_state, path):
        if current_state[0] == self.target or current_state[1] == self.target:
            print("Solution found:")
            for kk in range(len(path)):
                print(path[kk])
            return True

        self.visited_states.add(current_state)

        next_states = [
            (self.jug1_capacity, current_state[1]),  # Fill jug 1
            (current_state[0], self.jug2_capacity),  # Fill jug 2
            (0, current_state[1]),  # Empty jug 1
            (current_state[0], 0),  # Empty jug 2
            (min(current_state[0] + current_state[1], self.jug1_capacity), max(0, current_state[0] + current_state[1] - self.jug1_capacity)),  # Pour from jug 2 to jug 1
            (max(0, current_state[0] + current_state[1] - self.jug2_capacity), min(current_state[0] + current_state[1], self.jug2_capacity))  # Pour from jug 1 to jug 2
        ]

        for next_state in next_states:
            if next_state not in self.visited_states and self.is_valid_state(next_state):
                if self.dfs(next_state, path + [next_state]):
                    return True

        return False

    def solve(self):
        initial_state = (0, 0)
        self.dfs(initial_state, [initial_state])


# Example usage:
if __name__ == "__main__":
    jug1_capacity = 4
    jug2_capacity = 3
    target = 2
    problem = WaterJugProblem(jug1_capacity, jug2_capacity, target)
    problem.solve()
