class MyRange:
  def __init__(self, n):
    self.i = 0
    self.n = n
  
  def __iter__(self):
    return self
  
  def __next__(self):
    if self.i < self.n:
      i = self.i
      self.i += 1
      return i
    else:
      raise StopIteration()
    
class reverse_iter:
  def __init__(self, n):
    self.n = n
  
  def __iter__(self):
    return self
  
  def __next__(self):
    if len(self.n) > 0:
      return self.n.pop()
    else:
      raise StopIteration()
  
data_iter = MyRange(3)
print(next(data_iter))
print(next(data_iter))
print(next(data_iter))

data_reverse = reverse_iter([1,2,3,4])
print((next(data_reverse)))
print((next(data_reverse)))
print((next(data_reverse)))
print((next(data_reverse)))