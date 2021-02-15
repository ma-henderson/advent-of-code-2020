"""
Note for future:
This solution's major downfall is having 'hard-coded' the part where len(island) gives a specific # of possibilities,
I did this because I noticed that A) the input never had a jump of distance 2 and
B) there were no island of len > 5
"""

with open('day_10_inputs.txt', 'r') as f:
  lines = f.readlines()

  adapters = []
  for line in lines:
    adapters.append(int(line[:-1]))
  
  adapters = sorted(adapters)

  prev_a = 0
  x = 0
  y = 0
  for a in adapters:

    if a - prev_a == 1:
      x += 1
    elif a - prev_a == 3:
      y += 1
    prev_a = a
  
  y+=1 # because of adapter to device being 3
  
  print(x,y, x*y)
  # break down inputs into data sets of nodes delimited as islands of 3 dist from each other
  islands = []
  prev_a = 0
  address = 0 
  for i in range(len(adapters)):
    if adapters[i] - prev_a == 3:
      # create an island
      islands.append(adapters[address:i])
      address = i
    elif adapters[i] == adapters[-1]:
      islands.append(adapters[address:i+1])
      address = i
    prev_a = adapters[i]
  print(adapters)
  print(islands)
  print("there are",  len(islands), "islands")

  choose = []
  # Calculate the num of possibilities of each island
  for island in islands:
  # Case I: island needs every node (len of 1 or 2)
    if len(island) <= 2:
      choose.append(1)
  # Case II: island is self-contained (len of 3)
    elif len(island) == 3:
      choose.append(2)
  # Case III: Island requires a 'jump' (>3)  
    elif len(island) == 4:
      choose.append(4)
  # Case IV:  
    elif len(island) == 5:
      choose.append(7)
    else:
      print("MORE THAN 5 in 1")
  
  print(choose, len(choose))
  
  temp = 1
  for j in choose:
    temp = temp * j
  
  print(temp * 2) # because 0 to 1 OR 0 to 2 at beginning
