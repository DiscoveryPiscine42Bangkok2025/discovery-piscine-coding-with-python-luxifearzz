#!/usr/bin/python3

number = 0

while (number <= 10):
    multiplier = 0
    print(f"Table de {number}:", end="")
    while (multiplier <= 10):
        print("", number * multiplier, end="")
        multiplier += 1
    print()
    number += 1
