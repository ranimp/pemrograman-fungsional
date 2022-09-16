data = {'name': 'superman', 'last_name': 'hero', 'job': 'manager'}
data2 = {'name': 'batman', 'last_name': 'hero', 'job': 'CEO'}

# zipping
for (k1, v1), (k2, v2) in zip(data.items(), data2.items()):
  print(f'k1 {k1} -> {v1}')
  print(f'k2 {k2} -> {v2}')

# unzipp
pairs = [(1, 'a'), (2, 'b'), (3, 'b')]
numbers, letters = zip(*pairs)
print(numbers)
print(letters)

# sorting in paralel
letters = ['b', 'a', 'd', 'c']
numbers = [2, 4, 3, 1]
data1 = list(zip(letters, numbers))
print(data1)
data1.sort()
print(data1)
data2 = list(zip(numbers, letters))
print(data2)
data2.sort()
print(data2)
