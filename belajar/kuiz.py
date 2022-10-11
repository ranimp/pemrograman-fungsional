from itertools import zip_longest
# Function to convert decimal number
# to binary using recursion
def DecimalToBinary(num):
	
	if num >= 1:
		DecimalToBinary(num // 2)
	print(num % 2, end = '')


# DecimalToBinary(5)

#zipping
data = ['a','b','c','d','e']
angka = [1,2,3,4,5,6]

def proses(x,y):
  return list(zip_longest(x, y, fillvalue='?'))

# print(proses(data, angka))

# quick sort desc
def quicksortdesc(digit):
  return sorted(digit, reverse=True)

print(quicksortdesc([4,1,5,6,1,3]))
