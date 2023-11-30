import numpy as np
from itertools import takewhile 
import string

points = [l for l in string.ascii_letters]

def get_input(file_name):
    with open(file_name) as f:
        lines = [line.rstrip() for line in f]
    return lines

def get_dupes(first, second):
    d = set()
    for i in list(first):
        if i in second:
            d.add(i)
    return list(d)

def get_dupes_three(first, second, third):
    one = get_dupes(first, second)
    two = get_dupes(second, third)
    return get_dupes(one, two)

def get_points(letter):
    return points.index(letter) +1

def part1():
    dupes = []

    lines = get_input('./short.txt')
    for line in lines:
        halfway = len(line)//2
        first = line[:halfway]
        second = line[halfway:]
        dupes = dupes + ( get_dupes(first, second))
    print(dupes)
    sum = 0
    for d in dupes:
        s = get_points(d)
        print(d, s)
        sum += s
    print(sum)


def part2():
    points = [l for l in string.ascii_letters]
    dupes = []
    lines = get_input('./long.txt')
    sum = 0
    while len(lines) > 0:
        a, b, c = lines[:3]
        del lines[:3]
        d = get_dupes_three(a,b,c)[0]
        sum += get_points(d)
    print(sum)

    
part2()

