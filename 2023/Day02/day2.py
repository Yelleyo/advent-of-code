# only 12 red cubes, 13 green cubes, and 14 blue cubes
# check if game is possible, only possible games are to be added
# answer is all the possible games added up. 
#

# to check is a game is possible:
# add up the amount of each 3 colors, and compare with the valid_game values. 
# ading the amount for each colors: 
#   for each line:
#       for each char that is a bumber check 3 num later if r b g , add up to the corresponding one. 
#them elfs are putting those cubes back, each time separated by ;


input = 'day2inputtest2.txt'
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
    with open(input, 'r') as file:
        for line in file:
            line_format(line)
            for i in game_throws:
                throw_checker(i)
        if not 0 in line_check:
            valid_games += game_nb

    print(f"Amount of valid games: {valid_games}")

def line_format(line):
    global game_throws, game_nb
    game_nb = int(line.split(":")[0].split()[1])
    game_throws = line.split(":")[1].split(";")

def throw_checker(game_throws):
    global lb, lr, lg
    for throw in game_throws:
        for i, char in enumerate(throw.str()):
            if char.isdigit():
                if throw[i+2] == 'b':
                    lb = int((throw[i-1] + char).strip())
                    #print(f"{lb} blue")
                if throw[i+2] == 'r':
                    lr = int((throw[i-1] + char).strip())
                    #print(f"{lr} red")
                if throw[i+2] == 'g':
                    lg = int((throw[i-1] + char).strip())
                    #print(f"{lg} green")
        if lb <= vb and lr <= vr and lg <= vg:
            line_check.append(1)
            print(f"{game_nb} : this is a valid throw")
        else:
            line_check.append(0)
        lb = 0
        lr = 0
        lg = 0

def game_validator():
    if not 0 in line_check:
        valid_games += game_nb
        

validator()




