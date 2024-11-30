input_file = 'input_file.txt'
result = 0

with open(input_file, 'r') as file:
    content = file.read()
    max_cal = []
    blocks = content.strip().split("\n\n")
    for block in blocks:
        block_cal = 0
        lines = block.strip().split("\n")
        for line in lines:
            block_cal += int(line)
        max_cal.append(block_cal)
    print(max(max_cal))

    top3_cal = 0
    top3_cal += max(max_cal)
    max_cal.remove(max(max_cal))
    top3_cal += max(max_cal)
    max_cal.remove(max(max_cal))
    top3_cal += max(max_cal)
    max_cal.remove(max(max_cal))
    print(f'this is max3: {top3_cal}')


            