def sum_of_two(inputs, target):
  for i in range(len(inputs)):
    a = inputs[i]
    b = inputs[i:] # [i:] halves the qty of iterations
    b.remove(a)
    
    for j in b:
      if a + j == target and a != j:
        return False

  # return False if all checked and not yet returned a True
  return True


with open('day_9_inputs.txt', 'r') as f:
  lines = f.readlines()
  pre = 25

  rolling = []
  for item in lines[:pre]:
    rolling.append(int(item[:-1]))

  for i in range(pre, len(lines)):
    target = int(lines[i+1])
    
    if sum_of_two(rolling, target):
      n = target
      break

    rolling.pop(0)
    rolling.append(int(lines[i+1][:-1])) #[:-1] because python reads '\n' as 1 char

  print(i, n)

  ctp = [] # ctp for caterpillar
  for val in lines:
    ctp.append(int(val))

    # remove lower-end numbers until below n, while checking
    while sum(ctp) > n:
      ctp.pop(0)
    
    if sum(ctp) == n:
      print(max(ctp), min(ctp))
