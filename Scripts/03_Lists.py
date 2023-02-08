l = [1, 2, 3]

print("*** List iteration ***")
for item in l:
    print(item)

print("*** List comprehension ***")
print ([i+i for i in l if i %2 == 0])

print("*** List enumeration ***")
for index, item in enumerate(l):
    print(f"index: {index}, item: {item}")

print("*** Search list ***")
if 2 in l:
    print("list contains 2")

if 5 not in l:
    print("list does not contains 5")

print("*** List methods ***")
l.append(5)
print("Append: " + str(l))

l.insert(3, 9) 
print("Insert at position 3 the 9 " + str(l))

del l[2]
print("Delete item at position 2 " + str(l))

p = l.index(9)
print(f"9 is on position {p}")

l.sort()
print("list sorted " + str(l))

l.reverse()
print("list reversed " + str(l))
print(f"list contains {l.count(2)} items with value 2 ")



print("*** List slicing [start:end:step]***")

print("3rd items " + str(l[2]))
print("0-2 items " + str(l[0:2]))
print("First 3 items " + str(l[:3]))
print("Last 2 items " + str(l[-2:]))
print("All except the last 2 items " + str(l[:-2]))
print("Every second item " + str(l[1::2]))