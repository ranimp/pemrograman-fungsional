# konsep closure di pemrograman fungsional
def create_counter():
  count = 0
  
  def get_count():
    return count
  
  def increment():
    nonlocal count
    count += 1
    
  def reset():
    nonlocal count
    count = 0
  
  return (get_count, increment)

get_count, increment = create_counter()
print(get_count())
increment()
increment()
print(get_count())