numbers_list = [0,1,2,3,4,5,6,7,8,9]

# cara biasa
doubled_list = []
for x in numbers_list:
  doubled_list.append(x * 2)

print(doubled_list)

# cara dengan map
def double(x):
  return x * 2

double_list_functional = list(map(double, numbers_list))
print(double_list_functional)
                              