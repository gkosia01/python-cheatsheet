empty_set = set()
initiate_set = {1,2,3,4}

l = [5,6,6,6,6,7]
a= set(l)
print("a set: " + str(a))


print("*** iterate a set ***")
for i in a:
    print(i)


print("*** set comprehension ***")
scomp = {i for i in l if i%2 == 0}
print(str(scomp))


print("*** search a set ***")
if 3 in initiate_set:
    print("3 found in initiate_set")

print("*** add to a set ***")
a.add(8)
print("add: " + str(a))

print("*** remove to a set: raise KeyError if not found ***")
a.remove(8)
print("remove: " + str(a))

print("*** discard from a set: delete if exists ***")
a.discard(100)
print("discard: " + str(a))

print("*** set operations ***")

set_all = {1,2,3,4,5,6,7,8,9}
set_some = {1,2,3,10}

print(f"set_all does not contains common values with set_some: {str(set_all.isdisjoint(set_some))}")
print(f"set_all is subset of set_some: {str(set_all.issubset(set_some))}")
print(f"set_all is superset of set_some: {str(set_all.issuperset(set_some))}")
print(f"Union of two sets {str(set_all.union(set_some))}")
print(f"Intersection of two sets {str(set_all.intersection(set_some))}")
print(f"Difference of two sets {str(set_all.difference(set_some))}")