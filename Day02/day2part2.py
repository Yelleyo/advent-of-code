
line_check = []
sum_of_power = 0
pow_cube = 0
game_throws = []
game_nb = 0
vb = 14
vr = 12
vg = 13

lb = 0
lr = 0
lg = 0

min_blue = 0
min_red = 0
min_green = 0

def validator():
    global sum_of_power 
    with open('day2input.txt', 'r') as file:
        for line in file:
            line_format(line)
            for i in game_throws:
                min_cubes(i)
            game_power_cubes()
            print(f"pow cube: {power_cube}")
            sum_of_power += power_cube
            reset_min_cubes()

    print(f"Sum of pow of cubes: {sum_of_power}")

def line_format(line):
    global game_throws, game_nb
    game_nb = int(line.split(":")[0].split()[1])
    game_throws = line.split(":")[1].split(";")
    print(f"Game number: {game_nb}")
    print(f"Game_throws: {game_throws}")


def min_cubes(games_throws):
    global min_blue, min_red, min_green, pow_cube
    throws = games_throws.split(",")
    # print(throws)
    for throw in throws:
        # print(f"throw: {throw}")
        number, color = throw.strip().split(" ") # split at space
        number = int(number)
        # print(f"{color} {number}")
        if 'blue' in color and number > min_blue:
            min_blue = number
            #print(f"min_blue is now: {min_blue}")
        if 'red' in color and number > min_red:
            min_red = number
            #print(f"min_red is now: {min_red}")
        if 'green' in color and number > min_green:
            min_green = number
            #print(f"min_green is now: {min_green}")
    # print(f"Power cubes:\n blue: {min_blue}\n red: {min_red}\n green: {min_green}")

def game_power_cubes():
    global min_blue, min_red, min_green, power_cube
    power_cube = 1
    if min_blue != 0:
        power_cube *= min_blue
    if min_red != 0:
        power_cube *= min_red
    if min_green != 0:
        power_cube *= min_green
    return power_cube

def reset_min_cubes():
    global min_blue, min_red, min_green
    min_blue = 0
    min_red = 0
    min_green = 0

validator()