# Advent of Code 2024 - Day 7
# Author: Yelleyo

# always evaluated left-to-right
# only + or *
# split things 
# use product() from intertools to create all possible + and * combo depending on the amount nbs


import os
from itertools import product

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    with open('test.txt', 'r') as file:
        lines = file.read().splitlines()
    results = [line.strip().split(": ")[0] for line in lines]
    numbers = [line.strip().split(": ")[1] for line in lines]

    print(results)
    print(numbers)
    total = 0

    for result, numbers in zip(results, numbers):
        print(f'this result {result} goes with those numbers: {numbers}')
        nbs = numbers.strip().split(" ")
        print(nbs)
        target_result = int(result)
        if check_combinations(nbs, target_result):
            total += target_result

    print(f'Total: {total}')

def eval_left_to_right(expression):
    tokens = expression.split()
    result = int(tokens[0])
    i = 1
    while i < len(tokens):
        if tokens[i] == '+':
            result += int(tokens[i+1])
        elif tokens[i] == '*':
            result *= int(tokens[i+1])
        i += 2
    return result

def check_combinations(numbers, target_result):
    operators = ['+', '*']
    combinations = product(operators, repeat=len(numbers)-1)
    for ops in combinations:
        expression = " ".join(f"{num} {op}" for num, op in zip(numbers, ops + ('',)))
        if eval_left_to_right(expression.strip()) == target_result:
            print(f'Valid combination found: {expression.strip()} = {target_result}')
            return True
    return False


if __name__ == '__main__':
    main()


