import math

input_file = 'input.txt'
nodes = {}
steps = 0

with open(input_file, 'r') as file:
    lines = file.readlines()
    directions = lines[0].strip()

    for line in lines[2:]:
        key, values = line.split('=')
        values = values.strip('() \n')
        values = values.split(', ')
        nodes[key.strip()] = values

start_A = {}

for key in nodes.keys():
    if key.endswith('A'):
        start_A[key] = 1

# print(start_A)
# {'QKA': [], 'VMA': [], 'AAA': [], 'RKA': [], 'LBA': [], 'JMA': []}

for start in start_A:
    steps = 0
    node = start
    z_found = 0
    while True: 
        for i in directions:
            if i == 'L':
                node = nodes[node][0]
                steps += 1
            elif i == 'R':
                node = nodes[node][1]
                steps += 1
            if node.endswith('Z'):
                start_A[start] = steps
                z_found = 1
            print(node)
        if z_found:
            break

print(start_A)


def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b // math.gcd(a, b)

values = list(start_A.values())
lcm_value = values[0]
for value in values[1:]:
    lcm_value = lcm(lcm_value, value)

print(lcm_value)

# this is not working, not working.
# Maybe first make an array for the the first start value, and then
# check if those matches with the second, if good, check with third..
# 2 methods: 
# check make the steps together. 
# or amount of steps between two answers is a fixed number, can multiply this by each other.                                
