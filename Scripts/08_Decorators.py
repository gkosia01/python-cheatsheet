'''
    Decorators are wrappers of functions and can be used with @decor_name over the declaration of the funtion

'''

def logg(func):
    def inner(m1,m2):
        print("Start logging")
        func(m1,m2)
        print("Stop logging")
    return inner

@logg
def print_error(msg, msg2):
    print(msg + ' nnnn ' + msg2)


print_error("aaa", "bbb")
