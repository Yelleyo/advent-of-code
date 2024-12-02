import os
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

def main():
    with open('input.txt', 'r') as file:
        lines = file.read().splitlines()
        safe = 0
        
        for line in lines:
            numbers = line.split(" ")
            if check_line(numbers) or check_line_without_nb(numbers):
                    safe += 1

    print(f'Result safe: {safe}')

def check_line_without_nb(numbers):
    for i in range(len(numbers)):
        numbers_no_nb = numbers[:i] + numbers[i+1:]
        if check_line(numbers_no_nb):
            return True
    return False

def check_line(numbers):
    is_ascending = int(numbers[0]) < int(numbers[-1])  

    if is_ascending:
        for i in range(len(numbers) - 1):
            nb1 = int(numbers[i])
            nb2 = int(numbers[i + 1])
            if not (-3 <= nb1 - nb2 <= -1):
                return False
    else:
        for i in range(len(numbers) - 1):
            nb1 = int(numbers[i])
            nb2 = int(numbers[i + 1])
            if not (1 <= nb1 - nb2 <= 3):
                return False

    return True

if __name__ == '__main__':
    main()