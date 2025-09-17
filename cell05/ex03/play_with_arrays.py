#!/usr/bin/python3

original_array = [2, 8, 9, 48, 8, 22, -12, 2]
new_array = []

for num in original_array:
    if (num <= 5):
        continue
    new_array.append(num + 2)
new_array = set(new_array)

print("Original array:", original_array)
print("New array:", new_array)
