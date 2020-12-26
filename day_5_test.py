seat_input = "BFBBBBFRLL"

row = []
col = []
row.extend(range(128))
col.extend(range(8))

i = 0
for char in seat_input:
    
    # Find row
    if i < 7:
        sect = int(len(row)/2)
        if char == 'F':
            row = row[:sect]
        elif char == 'B':
            row = row[sect:]
    
    # Find Col
    else:
        sect = int(len(col)/2)
        if char == 'L':
            col = col[:sect]
        elif char == 'R':
            col = col[sect:]
    
    i+=1

print(row, col)

# /// Manual solution ///
# BFBBBBF - RLL

# B > 64-127
# F > 64-95
# B > 80-95
# B > 88-95
# B > 92-95
# B > 94-95
# F > 94

# R > 4-7
# L > 4-5
# L > 4