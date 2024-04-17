def countdown(n):
    while n > 0:
        yield n
        n -= 1

for i in countdown(5):
    print(i,"\n")

    


def my_generator(data):
    for item in data:
        yield item * 2

my_data = [1, 2, 3, 4, 5]

for item in my_generator(my_data):
    print(item)
