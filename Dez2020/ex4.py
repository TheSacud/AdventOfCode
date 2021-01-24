#!/usr/bin/python

with open('ex4.txt', 'r') as fd:
    content = fd.read()
    lines = content.split("\n\n")
    input = [line.replace("\n", " ") for line in lines]

def part1(input):
    good = 0
    passportValid = ["eyr", "hcl", "hgt", "byr", "iyr", "pid", "ecl"]
    for i in input:
        if all (x in i for x in passportValid):
            good += 1
    return good

print(part1(input))
