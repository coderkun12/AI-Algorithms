def get_possible_moves(state):
    moves = []
    for i in range(3):
        for j in range(3):
            if state[i][j] == '#':
                moves.append((i, j))
    return moves

def is_terminal(state):
    # Check rows
    for row in state:
        if row.count('X') == 3:
            return 'X'
        elif row.count('O') == 3:
            return 'O'

    # Check columns
    for j in range(3):
        if state[0][j] == state[1][j] == state[2][j] and state[0][j] != '#':
            return state[0][j]

    # Check diagonals
    if state[0][0] == state[1][1] == state[2][2] and state[0][0] != '#':
        return state[0][0]
    if state[0][2] == state[1][1] == state[2][0] and state[0][2] != '#':
        return state[0][2]

    # Check for draw
    if all(cell != '#' for row in state for cell in row):
        return 'Draw'

    return None

def evaluate(state):
    winner = is_terminal(state)
    if winner == 'X':
        return 10
    elif winner == 'O':
        return -10
    else:
        return 0

def minimax(state, depth, maximizing_player, level=0):
    if depth == 0 or is_terminal(state):
        return evaluate(state)

    if maximizing_player:
        max_eval = float('-inf')
        for move in get_possible_moves(state):
            i, j = move
            state[i][j] = 'X'
            print(f"{'  ' * level}New node generated at level {level}: {state}")
            eval = minimax(state, depth - 1, False, level + 1)
            state[i][j] = '#'  # undo move
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for move in get_possible_moves(state):
            i, j = move
            state[i][j] = 'O'
            print(f"{'  ' * level}New node generated at level {level}: {state}")
            eval = minimax(state, depth - 1, True, level + 1)
            state[i][j] = '#'  # undo move
            min_eval = min(min_eval, eval)
        return min_eval

# Test the implementation
start_state = [['X','O','X'],['O','#','O'],['#','X','#']]
print("Best score for the maximizing player:", minimax(start_state, 9, True))
