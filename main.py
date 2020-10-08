def personal_info(name, age):
  print(name, "is", age, "years old")

def calculation(x, y):
  return x+y, x-y

def mainFunction(a, b):
  def minorFunction(a,b):
    return a+b
  addition = minorFunction(a, b)
  return addition+5

def multlist(list):
  total = list[0]
  list.pop(0)
  for x in list:
    total *= x
  return total

print(multlist([1 ,2, 3 ,4]))


