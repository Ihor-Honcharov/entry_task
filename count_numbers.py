# The script covers the test task #1 
import re

input_data = 'numbers.txt'



def main():
    sum = 0
    with open(input_data, "r") as f:
        for line in f:
            number = re.findall(r'(^[+-]?(\d+(\.\d*)?|\d*\.\d+)([eE][+\-]?\d+)?$)', line.strip())
            if number:
                sum += float(number[0][0])

    print('Sum of the numbers in the file is: ', sum)
    print('Done')


if __name__ == "__main__":
    main()                   