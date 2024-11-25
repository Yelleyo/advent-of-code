import re

def main():
    with open('input.txt', 'r') as file, open('output.txt', 'w') as outfile:
        lines = file.read().splitlines()
        numbers = []
        characters = {}
        adjacent_numbers = {}

        for i, line in enumerate(lines):
            matches = re.finditer(r'\d+', line)
            for match in matches:
                numbers.append((i+1, match.start()+1, match.end(), int(match.group())))

            for j, char in enumerate(line):
                characters[(i+1, j+1)] = char

        # Now you can iterate over the characters.
        for position, char in characters.items():
            if char == '*':
                # Check the adjacent positions.
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        adjacent_position = (position[0] + dx, position[1] + dy)
                        if adjacent_position in characters and characters[adjacent_position].isdigit():
                            # If the adjacent character is a digit, find and print the whole number.
                            for number in numbers:
                                if number[0] == adjacent_position[0] and number[1] <= adjacent_position[1] <= number[2] + 1:
                                    if position not in adjacent_numbers:
                                        adjacent_numbers[position] = []
                                    if number[3] not in adjacent_numbers[position]: # Ensure the number is not already in the pair
                                        adjacent_numbers[position].append(number[3])

        # Calculate the total sum of the products of each pair of numbers.
        total_sum = 0
        for position, nums in adjacent_numbers.items():
            if len(nums) > 1:
                print(f'Numbers adjacent to * in line {position[0]} at position {position[1]}: {nums}')
                product = nums[0] * nums[1]
                total_sum += product
                print(f'Product of numbers: {product}')

        print(f'Total sum of all products: {total_sum}')
main()
