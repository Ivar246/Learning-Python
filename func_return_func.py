def outer_func():
    return 'hello world'
    def inner_func():
        print("Hello world")
    return inner_func


var = outer_func()
var()