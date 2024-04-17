def decor_wrap(f):
    def wrapper():
        print("before")
        f()
        print("after")
    return wrapper

@decor_wrap
def say_hello():
    print("hello")
say_hello()