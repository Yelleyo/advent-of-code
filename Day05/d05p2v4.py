inputs, *blocks = open('input.txt').read().split("\n\n")

inputs = list(map(int, inputs.split(":")[1].split()))
# print(inputs)

seeds = []

for i in range(0, len(inputs), 2):
    seeds.append((inputs[i], inputs[i] + inputs[i + 1]))

# print(f"Those are the seeds ranges: {seeds}")

for block in blocks:
    ranges = []
    for line in block.splitlines()[1:]:
        ranges.append(list(map(int, line.split())))
    converted_seeds = []
    while len(seeds) > 0:
        start, end = seeds.pop()
        for dest_start, source_start, range_length in ranges:
            overlap_start = max(start, source_start)
            overlap_end = min(end, source_start + range_length)
            if overlap_start < overlap_end:
                converted_seeds.append((overlap_start - source_start + dest_start, overlap_end - source_start + dest_start))
                if overlap_start > start:
                    seeds.append((start, overlap_start))
                if end > overlap_end:
                    seeds.append((overlap_end, end))
                break
        else:
            converted_seeds.append((start, end))
    seeds = converted_seeds


print(min(seeds)[0])