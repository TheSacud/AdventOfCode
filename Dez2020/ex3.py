#!/usr/bin/python
fn = "ex3.txt"
dat = open(fn).read().splitlines()

def colisoes(input, run, elevate):
    hit = 0
    x = 0
    y = 0
    while True:
        y = y + elevate
        if y >= len(input):
            break
        x = (x + run) % len(input[y])
        if input[y][x] == '#':
            hit += 1
    return hit

print(colisoes(dat,3,1))

def part2():
    result = 1
    for sploes in [[1,1],[3,1],[5,1],[7,1],[1,2]]:
        result = result * colisoes(dat,sploes[0],sploes[1])
    return result

print(part2())