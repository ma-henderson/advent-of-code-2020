# 128 rows
# 8 columns
# 0 index'd -> 0 to 127 rows and 0 to 7 col's

print("\n")
with open('day_5_inputs.txt', 'r') as f:
    seats = []

    for line in f:
        i = 0
        row = []
        col = []
        row.extend(range(128))
        col.extend(range(8))

        for char in line:
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

            i += 1
        seats.append({
            'row':row[0],
            'col':col[0]
        })

        

# print(seats)

seat_ids = []
for seat in seats:
    seat_ids.append(seat['row'] * 8 + seat['col'])

# print(max(seat_ids))
plane = sorted(seat_ids)
print(plane)

s_before = 1
for s in plane:
    if s - s_before > 1:
        print(s)
    s_before = s

# Seat id = row * 8 + column