'''
    arguments are passed by reference
'''

print("Lambda functions are inline functions")

l = lambda x, y: f" {x} and {y} formated by lambda"

print(l("3", "5"))


print("Closures are functions with inner function")

def is_even(number):
    
    def abs_the_input(a):
        if a < 0:
            return -1 * a
        return a
    
    return abs_the_input(number)

print(is_even(-30))