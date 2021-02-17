with open('day_11_inputs.txt', 'r') as f:
  lines = f.readlines()

  # set up seats:
  seats = []

  floor_row = []
  floor_row.extend("."*(len(lines[0])+1))
  floor_row = "".join(floor_row)

  # first 'fictitious' row
  seats.append(floor_row)
  for line in lines:
    # Add "floor" as a frame to all to fix for all special cases
    temp = []
    temp.append(".")
    temp.extend(line[:-1]) # -1 for '\n' char
    temp.append(".")
    temp = "".join(temp)

    seats.append(temp)
    
  # last 'fictitious' row
  seats.append(floor_row)

  for seat in seats:
    print(len(seat)) # 100 each, 98 + 1 on each side

  # Loop until no seats change state
  prev_seats = []
  flag = True
  k = 0
  while flag == True:
    k+=1
    i = 1 # Row Loc
    
    row_up = seats[i-1] # row_up updated within next loop
    new_seats = []
    new_seats.append(floor_row) # row 1
    for row in seats[1:-1]:
      # Create comparison rows for first, last, and all inbetween respectively
      row_down = seats[i+1]
      
      # Apply rules (simultaneously, not in cascade - slicing required)
      j = 1 # Column loc
      rc = row[:]

      new_row = [] # for simultaneous
      new_row.append('.') # pos 1
      for char in rc[1:-1]:
        # Establish adjacent seats within data-structure:
        adj = []
        adj.append(row_up[j-1]) # TL
        adj.append(row_up[j-0]) # TM
        adj.append(row_up[j+1]) # TR
        adj.append(rc[j+1]) # MR
        adj.append(row_down[j+1]) # BR
        adj.append(row_down[j-0]) # BM
        adj.append(row_down[j-1]) # BL
        adj.append(rc[j-1]) # ML
        

        # Rule 1: (i) Empty seat is always occupied (ii) if no adjacent seats are taken
        if char == "L" and len([True for s in adj if s != "#"]) == 8:
          new_row.append("#")
        # Rule 2: Occupied seat is vacated if >= 4 are occupied (#)
        elif char == "#" and len([True for s in adj if s == "#"]) >= 4:
          new_row.append("L")
        elif char == '.':
          new_row.append(".")
        # Else: seat does not change state
        else:
          new_row.append(char)
        j += 1
      new_row.append('.') # pos 100

      row_up = "".join(rc) # to make sure changes are done simultaneously
      
      # Create new temporary seats (only compared when done for simultaneous evaluations)
      new_seats.append("".join(new_row))
      i+=1

    new_seats.append(floor_row) #last row
    prev_seats = seats

    if new_seats == prev_seats:
      flag = False
    prev_seats = new_seats
    seats = new_seats

  for seat in seats:
    print(seat)
  print("iterations:", k)