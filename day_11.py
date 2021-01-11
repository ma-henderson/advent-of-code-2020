with open('day_11_inputs.txt', 'r') as f:
  lines = f.readlines()
  
  # set up seats:
  seats = []

  floor_row = []
  floor_row.extend("."*(len(lines[0])+2))
  floor_row = "".join(floor_row)

  # first 'fictitious' row
  seats.append(floor_row)
  for line in lines:
    # Add "floor" as a frame to all to fix for all special cases
    temp = []
    temp.append(".")
    temp.append(line[:-1])
    temp.append(".")
    temp = "".join(temp)

    seats.append(temp)
    
  # last 'fictitious' row
  seats.append(floor_row)

  # for seat in seats:
  #   print(seat)

  # Loop until no seats change state
  prev_seats = []
  while seats != prev_seats:
    i = 1 # Row Loc
    for seat in seats[1:-1]:
      # Create comparison rows for first, last, and all inbetween respectively
      seat_up = seats[i-1][:]
      seat_down = seat[i+1][:]
      
      # Apply rules (simultaneously, not in cascade - slicing required)
      j = 1 # Column loc
      for char in seat:
        # Establish adjacent seats within data-structure:
        adj = []
        adj.append(seats[i-1][j-1]) # TL
        adj.append(seats[i-1][j-0]) # TM
        adj.append(seats[i-1][j+1]) # TR
        adj.append(seats[i-0][j+1]) # MR
        adj.append(seats[i+1][j+1]) # BR
        adj.append(seats[i+1][j-0]) # BM
        adj.append(seats[i+1][j-1]) # BL
        adj.append(seats[i-0][j-1]) # ML
        
        # Rule 1: (i) Empty seat is always occupied (ii) if no adjacent seats are taken
        elif char == "L" and len([True for s in adj if s != "#"]) == 8:
          seat
        
      # Rule 2: Occupied seat is vacated if >= 4 are occupied
      # Else: seat does not change state
      j += 1



      i+=1
