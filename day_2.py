from day_2_inputs import inputs

def split(word):
  return [char for char in word]

ok_list = []
for item in inputs:
  p1 = int(item[0].split("-")[0])
  p2 = int(item[0].split("-")[1])
  target = item[1]
  pw = split(item[2])

  # needed for pt 1
  # temp = [letter for letter in pw if letter == target]
  
  # if len(temp) <= int(upper_limit) and len(temp) >= int(lower_limit):
    # ok_list.append(item[2])

  # Part 2:
  temp = 0
  if pw[p1-1] == target:
    temp += 1
  if pw[p2-1] == target:
    temp += 1
  if temp == 1:
    ok_list.append(item[2])
  
print(len(ok_list))
  