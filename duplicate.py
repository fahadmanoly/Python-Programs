my_list = [1, 2, 3, 2, 4, 3, 5, 6, 5,3]

seen = set()
print(seen)
duplicates = []

for element in my_list:
    if element in seen:
        duplicates.append(element)
    else:
        seen.add(element)

print(duplicates)  # Output: [2, 3, 5]
