print('\nPython\n')

one = 'Python 2023'
two = 'Python 2023'
three = 'Python 2023'

print(bool(one==two))
print(bool(two==three))

print(type(one),hex(id(one)))
print(type(two),hex(id(one)))
print(type(three),hex(id(one)))

print('\nJava\n')
three = 'Java 11'

print(bool(one==two))
print(bool(two==three))

print(type(one),hex(id(one)))
print(type(two),hex(id(two)))
print(type(three),hex(id(three)))