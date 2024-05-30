import numpy as np

# Define an empty matrix of size 7x11
size_v = 7
size_h = 11

number_of_paths = 2
min_path_length = 4
max_path_length = 8

level = np.zeros((size_h, size_v))


# Function to check if the position is valid (not touching borders or other paths)
def is_valid_position(level, x, y):
    if x <= 0 or x >= size_h - 1 or y <= 0 or y >= size_v - 1:
        return False
    if level[x, y] == 1:
        return False
    return True


# Function to generate a random path
def generate_path(level, path_length):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    while True:
        x, y = np.random.randint(1, size_h - 1), np.random.randint(1, size_v - 1)
        if is_valid_position(level, x, y):
            break
    path = [(x, y)]
    level[x, y] = 1

    while len(path) < path_length:
        np.random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = path[-1][0] + dx, path[-1][1] + dy
            if is_valid_position(level, nx, ny):
                path.append((nx, ny))
                level[nx, ny] = 1
                break
        else:
            # No valid move found, backtrack
            if len(path) > 1:
                path.pop()
            else:
                # Restart if we cannot make a path of the desired length
                for px, py in path:
                    level[px, py] = 0
                return False
    return True


# Generate paths
paths_generated = 0
attempts = 0
max_attempts = 1000 
while paths_generated < number_of_paths and attempts < max_attempts:
    path_length = np.random.randint(min_path_length, max_path_length + 1)
    if generate_path(level, path_length):
        paths_generated += 1
    attempts += 1

# print(level)

# Change the matrix into string represented by '..' and 'XX' for empty and path respectively
level_str = ''
for row in level:
    for cell in row:
        level_str += 'XX' if cell == 1 else '..'
    level_str += '\n'

print(level_str)