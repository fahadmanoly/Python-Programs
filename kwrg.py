def my_function(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

my_function(name='Alice', age=30, city='New York')
