with open('day_8_input.txt', 'r') as f:
  # Set up base dictionary
  lines = f.readlines()
  data = {}
  for i, n in enumerate(lines):
    data[i] = n[:-1]

  print(data)
  # Set up result variables
  acc = 0
  line_log = []
  flag = True

  # Start
  adr = 0
  while flag == True:
    if adr in line_log:
      flag = False    

    # After checking if repeated, add adr to log
    line_log.append(adr)

    # set up line's values
    c = data[adr].split()[0]
    n = data[adr].split()[1]
    
    if c == 'acc':
      if n[0] == '+':
        acc += int(n[1:])
      elif n[0] == '-':
        acc -= int(n[1:])
      adr += 1

    elif c == 'jmp':
      if n[0] == '+':
        adr += int(n[1:])
      elif n[0] == '-':
        adr -= int(n[1:])

    elif c == 'nop':
      adr += 1

    # Testing
    else:
      print('fail in reading c:', c)
  
  print(acc, line_log)
