'''
    Iterators are classes that implement the __iter__() function
    The remember the last with a variable in the class
    We use next() to ge the next item
    Throw StopIteration after the last
'''

iteror = iter('ABCDEF')

print(f"The next is {next(iteror)}")


'''
    Generators: are functions that can post and resume.
                they generate the value when needed
'''

def gen_numbers(x):

    indx = 1
    while indx < x:
        yield indx

        indx+=1

gen_1000 = gen_numbers(1000)

print(f"Get first {next(gen_1000)} get other {next(gen_1000)} for generator")


print("Can build generators comprehensions if replace [ with ( ")

gen_comprehens = (i for i in range(100))

print(f"Get first {next(gen_comprehens)} get other {next(gen_comprehens)} for generator comprehension")
