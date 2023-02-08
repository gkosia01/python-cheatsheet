msg = "Its a nice day"
print(msg.upper())
print('__'.join(['Join', 'List', 'With', 'Specific', 'Character']))
print('multiply by 3' * 3)

if ' a ' in msg:
    print("a is in msg")

for letter in '123':
    print("for: " + letter)

for indx, letter in enumerate('123'):
    print(f"enumerate: index: {indx}, letter{letter}")


print("find: " + str(msg.find('nice')))
print("endswith: " + str(msg.endswith('day')))
print(msg.split(' '))
print("Strip: " + "  msg   ".strip())
