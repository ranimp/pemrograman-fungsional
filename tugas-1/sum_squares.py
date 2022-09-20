# menggunakan list comprehension
t = (1,2,3)

def sumOfSquares(t):
  return sum([i*i for i in t])

print(sumOfSquares(t))
print(sumOfSquares([1,2,3]))