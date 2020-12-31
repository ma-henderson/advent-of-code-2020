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

# day_7 = 'faded bronze bags contain 2 light salmon bags.'
# in_index = day_7.find('contain')
# in_count = in_index + 8
# in_color = day_7[in_count + 2,]
# print(in_index, day_7[in_index + 8])

test_dict = {}

# test_dict['key'] = []
# test_dict['key'].append(123)
# test_dict['key'] = []
# print(test_dict)

# inc_color = 'light blue'
# inc_cap = 2

# test_dict[f'{inc_color}'] = inc_cap
# print(test_dict)

test_dict['blue'] = {'red': 1}
test_dict['brown'] = {'green': 1}
test_dict['black'] = {'yellow': 1}

for col in test_dict:
    if any([True for key in test_dict[col].keys() if key == 'red']):
        print(True, f"for {col}")
    else:
        print(False, f"for {col}")