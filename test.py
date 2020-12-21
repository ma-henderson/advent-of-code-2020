some_string = "iyr:2015 ecl:gry"
split_string = some_string.split(" ")

for i in split_string:
    if "iyr" in i:
        print("success")
