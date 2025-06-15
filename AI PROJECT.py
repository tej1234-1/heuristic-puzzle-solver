import heapq

goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

def find_position(puzzle, value):
    for row in range(3):
        for col in range(3):
            if puzzle[row][col] == value:
                return row, col

def manhattan_distance(current_state):
    distance = 0
    for row in range(3):
        for col in range(3):
            value = current_state[row][col]
            if value != 0:
                goal_row, goal_col = find_position(goal_state, value)
                distance += abs(row - goal_row) + abs(col - goal_col)
    return distance

def get_next_states(state):
    neighbors = []
    row, col = find_position(state, 0)
    moves = [(-1,0), (1,0), (0,-1), (0,1)]
    for move in moves:
        new_row = row + move[0]
        new_col = col + move[1]
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_state = [r[:] for r in state]
            new_state[row][col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[row][col]
            neighbors.append(new_state)
    return neighbors

def is_goal(state):
    return state == goal_state

def convert_to_tuple(state):
    return tuple(tuple(row) for row in state)

def solve_puzzle(start_state):
    priority_queue = []
    heapq.heappush(priority_queue, (manhattan_distance(start_state), 0, start_state, []))
    visited = set()
    while priority_queue:
        f, g, current_state, path = heapq.heappop(priority_queue)
        if is_goal(current_state):
            return path + [current_state]
        visited.add(convert_to_tuple(current_state))
        for next_state in get_next_states(current_state):
            if convert_to_tuple(next_state) not in visited:
                new_path = path + [current_state]
                h = manhattan_distance(next_state)
                heapq.heappush(priority_queue, (g + 1 + h, g + 1, next_state, new_path))
    return None

def print_board(state):
    for row in state:
        print(" ".join(str(val) if val != 0 else "_" for val in row))
    print()

start_state = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

solution_steps = solve_puzzle(start_state)

if solution_steps:
    print("✅ Puzzle solved in", len(solution_steps) - 1, "moves.\n")
    for index, state in enumerate(solution_steps):
        print(f"🔹 Step {index}:")
        print_board(state)
else:
    print("❌ No solution found.")
