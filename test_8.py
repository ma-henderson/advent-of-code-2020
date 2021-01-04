# with open('day_8_input.txt', 'r') as f:
#   print(type(f))
#   lines = f.readlines()
#   print(lines[:10])
  
#   data = {}
#   for i, n_lines in enumerate(lines[:10]):
#     print(i, n_lines[:-2])
#     data[i] = n_lines[:-2]
#   print(data)

  
def some_fn():
  a = 'hello'
  b = 'world'
  return a,b

s1, s2 = some_fn()
print(s1, s2)

s = some_fn()
print(type(s))