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

node = 'AAA'

while True:
    for i in directions:
        if i == 'L':
            node = nodes[node][0]
            steps += 1
            print(node)
        elif i == 'R':
            node = nodes[node][1]
            steps += 1
            print(node)
        if node == 'ZZZ':
            print(steps)
            exit(0)