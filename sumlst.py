list1 = [1, 2, 3]
list2 = [4, 5, 6]

result = []

for a, b in zip(list1, list2):
    result.append(a + b)

print(result)  # Output: [5, 7, 9]
