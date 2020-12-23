import re
some_string = "#18301f"
pattern = '^#[a-f0-9]{6}'

print(re.match(pattern, some_string))

if not True:
    print('yes')