def put_exception(fn):
    def ex(t):
        print(t)
        try:
            fn(6)
        except Exception as e:
            print(e)
        #    traceback.print_exc()

    return ex


@put_exception
def a(text):
    print(text)


a(1)
