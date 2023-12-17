# add up the last val of each array. 

input_file = 'input.txt'

result = ''

sum_total = 0
with open(input_file, 'r') as file:
    lines = file.readlines()
    total = 0
    for line_nb, line in enumerate(lines, 1):
        string_values = line.split(' ')
        values = [int(value) for value in string_values]
        print(f'This is line {line_nb}')
        print(values)

        line_arrays = []
        new_row = []
        line_arrays.insert(0, values)

        while True:
            for i in range(1, len(values)):
                new_row.append(values[i] - values[i - 1])
            values = new_row
            new_row =[]
            line_arrays.insert(0, values)
            print(values)

            if all(value == 0 for value in values) or len(values) == 1:
                # print("all values in the array are 0")
                break
        # print(f'Those are the arrays for this line {line_nb}: {line_arrays}')
        #print(line_arrays)
        last_nb = [array[-1] for array in line_arrays]
        #print(last_nb)

        sum_line = sum(last_nb)
        #print(sum_line)
        sum_total += sum_line
print(sum_total)
# 1641934234


