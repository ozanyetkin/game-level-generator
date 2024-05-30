import numpy as np
import string

# Define an empty matrix of size 7x11
size_v = 7
size_h = 11

number_of_paths = 3
min_path_length = 4
max_path_length = 8

level = np.zeros((size_h, size_v), dtype=object)


# Function to check if the position is valid (not touching borders or other paths)
def is_valid_position(level, x, y, allow_adjacent=False):
    if x <= 0 or x >= size_h - 1 or y <= 0 or y >= size_v - 1:
        return False
    if level[x, y] != 0:
        return False
    if not allow_adjacent and any(
        level[nx, ny] != 0
        for nx in range(x - 1, x + 2)
        for ny in range(y - 1, y + 2)
        if 0 <= nx < size_h and 0 <= ny < size_v
    ):
        return False
    return True


# Function to generate a random path
def generate_path(level, path_length, path_char):
    while True:
        x, y = np.random.randint(1, size_h - 1), np.random.randint(1, size_v - 1)
        if is_valid_position(level, x, y):
            break
    path = [(x, y)]
    level[x, y] = "XX"
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

    current_char = path_char
    while len(path) < path_length:
        np.random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = path[-1][0] + dx, path[-1][1] + dy
            if is_valid_position(level, nx, ny, allow_adjacent=True):
                path.append((nx, ny))
                level[nx, ny] = f"{current_char}."
                current_char = chr(ord(current_char) + 1)
                if current_char > "z":
                    current_char = "a"
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
max_attempts = 1000  # Max attempts to prevent infinite loop
path_char = "a"
while paths_generated < number_of_paths and attempts < max_attempts:
    path_length = np.random.randint(min_path_length, max_path_length + 1)
    if generate_path(level, path_length, path_char):
        paths_generated += 1
        # Move to the next starting character for the next path
        path_char = chr(ord(path_char) + path_length + 1)
        if path_char > "z":
            path_char = "a"
    attempts += 1

# Convert level to string representation
level = np.array(level, dtype=object)
level[level == 0] = ".."

# Print the matrix as a string
for row in level:
    print("".join(row))
