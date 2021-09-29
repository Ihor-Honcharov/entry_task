# python .\sum_numbers\map-reduce.py
# 10 20 35 [Enter]

from functools import reduce

#x, y, z = input().strip().split()
#x, y, z = map(int, (x, y, z))
'''
x, y, z = map(int, input().strip().split())
volume = x * y * z
print(f"{x=}, {y=}, {z=}, {volume=}")
'''
volume = reduce(
    lambda x, y: x * y,
    map(int, input().strip().split())
)
print(f"{volume=}")
print("Done")
