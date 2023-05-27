def deco(func):
    print("装饰外部函数")

    def a():
        print(6)

    def inner():
        a()
        func()
        return "内部函数"

    print("外部函数")
    return inner


@deco
def myfunc():
    print("myfunc")


# myfunc = deco(myfunc)
myfunc()
