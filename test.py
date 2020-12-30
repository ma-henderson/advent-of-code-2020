# l = []
# l.extend(range(10))

# print(l)
# l = l[5:]
# print(l)

# # Truncates it when int()
# n = 3
# print(int(n/2))


# day_6 = 'accddeeffhhijjkkllmmnnoopprrttvvxxyyzz'
# print(day_6.count('J'))

day_7 = 'faded bronze bags contain 2 light salmon bags.'
in_index = day_7.find('contain')
in_count = in_index + 8
in_color = day_7[in_count + 2,]
print(in_index, day_7[in_index + 8])