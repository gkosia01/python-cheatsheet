simple_dictionary = {1: 'A', 2:'B', 3:'C'}

print("*** Convert list to dict ***")
l = ['Aa', 'Bb', 'Cc']
d = dict(zip(range(len(l)),l))
print(str(d))

print("*** Convert string pairs to dict ***")
string_pairs = "1=a,2=b,3=c"
di = dict(i.split("=") for i in string_pairs.split(","))
print(str(di))


print("*** dict comprehensions ***")
a = {key:val + val for key,val in simple_dictionary.items()}
print(str(a))


print("*** count number of times of value in list as dict ***")
lst = [1,2,3,4,4,4,4,5,5,6]
result = {k: lst.count(k) for k in set(lst)}
print(str(result))

print("*** iter on dictionary ***")

print("*** iter on keys ***")
for k in result.keys():
    print(k)
print("*** iter on pairs ***")
for k,v in result.items():
    print(k,v)
print("*** iter on values ***")
for v in result.values():
    print(v)


print("*** dict functions ***")

print(f"Get value of specific key else default {simple_dictionary.get(4, 'Key 4 not found')}")
print(f"Remove {simple_dictionary.pop(2,'Key 2 not found')} from dictionary")

simple_dictionary[6] = 'ZZZ'
print(str(simple_dictionary))