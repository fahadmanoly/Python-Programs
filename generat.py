def count_up_to(n):
    i = 0
    while i <= n:
        yield i
        i += 1
for num in count_up_to(5):
    print(num)
