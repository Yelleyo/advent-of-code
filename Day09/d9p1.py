input_file = 'input.txt'

result = ''


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

        num = 0
        for i in range(len(line_arrays) - 1):
            num = line_arrays[i][-1] + line_arrays[i + 1][-1]
            line_arrays[i + 1].append(num)
            print(line_arrays[i + 1])
    
        total += num
    print(total)
        
    







