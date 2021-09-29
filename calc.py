input_data = 'numbers.txt'

with open(input_data, "r") as f:
    result = sum(float(line) for line in f if line.strip().isnumeric())

print(result)