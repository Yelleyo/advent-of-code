line_check = []
valid_games = 0
game_throws = []
game_nb = 0
vb = 14
vr = 12
vg = 13

lb = 0
lr = 0
lg = 0


def validator():
    global valid_games 
    with open('day2input.txt', 'r') as file:
        for line in file:
            line_format(line)
            for i in game_throws:
                throw_checker(i)
            if not 0 in line_check:
                print(f"Game {game_nb} is valid")
                valid_games = game_nb + valid_games
                print(f"Valid game count: {valid_games}")
            line_check.clear()

    print(f"Valid games nb added up: {valid_games}")

def line_format(line):
    global game_throws, game_nb
    game_nb = int(line.split(":")[0].split()[1])
    print(f"Game number: {game_nb}")
    game_throws = line.split(":")[1].split(";")

def throw_checker(game_throws):
    global lb, lr, lg
    # Break down each throw into color and number
    throws = game_throws.split(",")
    print(f"those are the throws {throws} ")
    for throw in throws:
        # Get color and number from each throw
        number, color = throw.strip().split(" ") # split at space
        number = int(number)
        if 'blue' in color:
            lb = number
        elif 'red' in color:
            lr = number
        elif 'green' in color:
            lg = number
    # Check if all colors are within the limit
    if lb <= vb and lr <= vr and lg <= vg:
        line_check.append(1)
    else:
        line_check.append(0)
    lb = 0
    lr = 0
    lg = 0


validator()