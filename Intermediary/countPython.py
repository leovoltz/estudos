from itertools import count

c1 = count(8, 8)
r1 = range(8, 100, 8)

# for i in c1:
# print()


print('c1', hasattr(c1, '__iter__'))
print('c1', hasattr(c1, '__next__'))
print('r1', hasattr(r1, '__iter__'))
print('r1', hasattr(r1, '__next__'))

for i in c1:
    if i >= 100:
        break

    print(i)
print()
print('range')
for i in r1:
    print(i)
