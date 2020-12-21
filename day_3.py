from day_3_inputs import inputs
sequence = []
hit_count = 0
miss_count = 0
x = 0
y = 0
x_step = 1
y_step = 2

# start
for i in range(0,len(inputs),y_step):
  if x > len(inputs[i]) - 1:
    x -= len(inputs[i])
  sequence.append(i)

  if inputs[i][x] == "#":
    hit_count += 1
  else:
    miss_count += 1
  x += x_step

print('hit count', hit_count, 'for x_step of', x_step)
print('for y_step of', y_step)
# print('miss count', miss_count)
print(sequence)