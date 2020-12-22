import re
some_string = "#12301f"
pattern = '^#[a-f0-9]{6}'

print(re.match(pattern, some_string))

if not True:
    print('yes')