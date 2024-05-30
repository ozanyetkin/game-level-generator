import numpy as np

# Define an empty matrix of size 7x11
size_v = 7
size_h = 11

number_of_paths = 3
min_path_length = 4
max_path_length = 8

level = np.zeros((size_h, size_v))

# Generate random continuous (can be non-linear) paths represented by 1
# Line paths should have a minimum length of min_path_length and a maximum length of max_path_length
# Paths should not be crossing each other
for i in range(number_of_paths):
    # Randomly select the starting point of the path
    start = np.random.randint(0, size_h)
    # Randomly select the ending point of the path
    end = np.random.randint(0, size_h)
    # Randomly select the path type (linear or non-linear)
    path_type = np.random.randint(0, 2)
    # Generate the path
    if path_type == 0:
        # Generate a linear path
        if start < end:
            level[start:end+1, i] = 1
        else:
            level[end:start+1, i] = 1
    else:
        # Generate a non-linear path
        level[start, i] = 1
        level[start+1, i] = 1
        level[end, i] = 1
        level[end-1, i] = 1


# Replace the path with 0 and 1 with ' ' and 'X' respectively
level = np.where(level == 0, '..', 'XX')

# Print the path with ' ' and 'X'
print(level)