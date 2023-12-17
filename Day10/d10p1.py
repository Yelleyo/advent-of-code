input_file = 'input.txt'

lines = []

# Put input into an array of lines
with open(input_file, 'r') as file:
    for line in file:
        lines.append(line.strip())

# Find the start
for i, line in enumerate(lines):
    if 'S' in line:
        found = True
        start_position = {'value': 'S', 'line': i, 'index': line.index('S')}
        break

print('Start position: ', start_position)

# Initialize the positions dictionary with the current position
positions = {'previous': start_position, 'current': None}

# Check start UP
if start_position['line'] > 0 and lines[start_position['line'] - 1][start_position['index']] in ('F', '7', '|'):
    positions['current'] = {
        'value': lines[start_position['line'] - 1][start_position['index']],
        'line': start_position['line'] - 1,
        'index': start_position['index']
    }

# Check start Down
elif lines[start_position['line'] + 1][start_position['index']] in ('L', 'J', '|'):
    positions['current'] = {
        'value': lines[start_position['line'] + 1][start_position['index']],
        'line': start_position['line'] + 1,
        'index': start_position['index']
    }

# Check start left
elif start_position['index'] > 0 and lines[start_position['line']][start_position['index'] - 1] in ('F', 'L'):
    positions['current'] = {
        'value': lines[start_position['line']][start_position['index'] - 1],
        'line': start_position['line'],
        'index': start_position['index'] - 1
    }

# Check start right
elif lines[start_position['line']][start_position['index'] + 1] in ('J', '7'):
    positions['current'] = {
        'value': lines[start_position['line']][start_position['index'] + 1],
        'line': start_position['line'],
        'index': start_position['index'] + 1
    }

print('Positions: ', positions)

# Now we move on depending on where we came from
# Until we hit S again


def down(positions):
    positions['previous'] = positions['current']
    positions['current'] = {
        'value': lines[positions['current']['line'] + 1][positions['current']['index']],
        'line': positions['current']['line'] + 1,
        'index': positions['current']['index']
    }
def up(positions):
    positions['previous'] = positions['current']
    positions['current'] = {
        'value': lines[positions['current']['line'] - 1][positions['current']['index']],
        'line': positions['current']['line'] - 1,
        'index': positions['current']['index']
    }
def right(positions):
    positions['previous'] = positions['current']
    positions['current'] = {
        'value': lines[positions['current']['line']][positions['current']['index'] + 1],
        'line': positions['current']['line'],
        'index': positions['current']['index'] + 1
    }
def left(positions):
    positions['previous'] = positions['current']
    positions['current'] = {
        'value': lines[positions['current']['line']][positions['current']['index'] - 1],
        'line': positions['current']['line'],
        'index': positions['current']['index'] - 1
    }
steps = 1
while True:
    if positions['current']['value'] == '|' and positions['current']['line'] > positions['previous']['line']:  # | Go down
       down(positions) 
    elif positions['current']['value'] == '|' and positions['current']['line'] < positions['previous']['line']:  # | Go Up
        up(positions)
    elif positions['current']['value'] == 'L' and positions['current']['line'] > positions['previous']['line']:  # L Go right   
        right(positions)
    elif positions['current']['value'] == 'L' and positions['current']['line'] == positions['previous']['line']:  # L Go up
        up(positions)
    elif positions['current']['value'] == '-' and positions['current']['index'] < positions['previous']['index']:  # - Go left
        left(positions)
    elif positions['current']['value'] == '-' and positions['current']['index'] > positions['previous']['index']:  # - Go right
        right(positions)
    elif positions['current']['value'] == 'J' and positions['current']['line'] == positions['previous']['line']:  # J Go up
        up(positions)
    elif positions['current']['value'] == 'J' and positions['current']['line'] > positions['previous']['line']:  # J Go left
        left(positions)
    elif positions['current']['value'] == 'F' and positions['current']['line'] < positions['previous']['line']:  # f Go right
        right(positions)
    elif positions['current']['value'] == 'F' and positions['current']['line'] == positions['previous']['line']:  # f Go down
        down(positions)
    elif positions['current']['value'] == '7' and positions['current']['line'] < positions['previous']['line']:  # 7 Go left
        left(positions)
    elif positions['current']['value'] == '7' and positions['current']['line'] == positions['previous']['line']:  # 7 Go down
        down(positions)

    elif positions['current']['value'] == 'S':
        break

    print(positions)
    steps += 1
half_steps = steps / 2
print('Final Positions: ', positions)
print('Amount of steps: ', steps)
print('Answer: ', half_steps)
