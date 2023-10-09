def view_show_decorator(fn):
    def decorator():
        fn()

    return decorator


@view_show_decorator
def do_something():
    print('我做一些事')




def run():
    do_something()


run()
