
input_file = 'input2.txt'
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

start_A = []

for key in nodes.keys():
    if key.endswith('A'):
        start_A.append(key)

print(start_A)

current_node = ''
node_dict = {}

y =0
while y <= 2:
    for start in start_A:
        node_dict[start] = []
        current_node = start
        for i in directions:
            if current_node.endswith('Z'):
                node_dict[start].append(i)
            if i == 'L':
                current_node = nodes[current_node][0]
                print(current_node)
            elif i == 'R':
                current_node = nodes[current_node][1]
                print(current_node)
            steps += 1
    y += 1

print(node_dict)