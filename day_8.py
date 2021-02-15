def day8_data():
  with open('day_8_inputs.txt', 'r') as f:
    # Set up base dictionary
    lines = f.readlines()
    data = {}
    for i, n in enumerate(lines):
      data[i] = n[:-1]

    return data

def day8_p1(data):  
  # Set up result variables
  acc = 0
  line_log = []
  flag = True

  # Start
  adr = 0
  while flag == True:
    # for Part 2:
    if adr >= len(data.keys()):
      print("Booted succesfully by changing address", adr)
      # append to log for checking
      line_log.append(adr)
      return acc, line_log

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

  return acc, line_log

data_dict = day8_data()
acc, line_log = day8_p1(data_dict)

# Part 2:
for adr in line_log:
  # set up line's values
  c = data_dict[adr].split()[0]
  n = data_dict[adr].split()[1]
  # keep a copy in case it doesn't fix the issue
  temp_v = data_dict[adr]

  # print(adr)

  if c == 'jmp':
    # change jmp to nop command
    data_dict[adr] = ' '.join(['nop', n])
  elif c == 'nop':
    # change nop to jmp
    data_dict[adr] = ' '.join(['jmp', n])
  
  # run the program and see if it ends succesfully
  acc, line_log_t = day8_p1(data_dict)
  # last number > len means it terminated succ.
  if line_log_t[-1] > list(data_dict.keys())[-1]:
    print("\n", acc)
  else:
    data_dict[adr] = temp_v
  
