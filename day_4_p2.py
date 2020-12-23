import re
with open('day_4_inputs.txt', 'r') as f:
    counter = 0
    doc_start_indices = [0] # first entry is @ 0
    prev_char = ''

    data = []
    temp = []
    
    # note CID is not included
    req_fields = [
        'byr',
        'iyr',
        'eyr',
        'hgt', 
        'hcl',
        'ecl',
        'pid',
    ]

    eyc_list = [
        'amb',
        'blu',
        'brn',
        'gry',
        'grn',
        'hzl',
        'oth'
    ]

    
    accepted_list = []
    rejected_list = []
    ok = False

    for line in f:
        for char in line:
            # identify new document entry:
            if  char == '\n' and prev_char == '\n':
                doc_start_indices.append(counter+1)
                
                # Append the entirety of previously parsed info into DATA as a single list
                data.append(" ".join(temp))
                # Clear temp list to combine lines of data into list
                temp = []

            # identify line of data entry:
            elif char == '\n' and prev_char != '\n' and prev_char != ' ':
                # take the entire line
                temp.append(line[:-1]) #[:-2] avoids taking \n with it
            prev_char = char
        counter += 1
    


    for elem in data[:10]:
        # turn string into list of kv-pairs
        kv_pairs = elem.split(" ")

        # //// Part 2 //// 
        # Creating a dictionary
        keys = [segment.split(":")[0] for segment in kv_pairs]
        values = [segment.split(":")[1] for segment in kv_pairs]
        td = {}
        
        # /// for Debugging:
        print("\n", kv_pairs)
        # print(keys)
        # print(values)

        for i in range(len(kv_pairs)):
            td[keys[i]] = values[i]
        
        print(td)

        # contains all required fields? (PART 1)
        if all([True if field in keys else False for field in req_fields]):

            # required fields in correct format? (PART 2)
            if len(td['byr']) != 4 or int(td['byr']) < 1920 or int(td['byr']) > 2002:    
                print("Failed byr test")
                # rejected_list.append(td)
                continue
            if len(td['iyr']) != 4 or int(td['iyr']) < 2010 or int(td['iyr']) > 2020:    
                print("Failed iyr test")
                # rejected_list.append(td)
                continue
            if len(td['eyr']) != 4 or int(td['eyr']) < 2020 or int(td['eyr']) > 2030:    
                print("Failed eyr test")
                # rejected_list.append(td)
                continue
            if td['hgt'][-2:] == 'cm':
                if int(td['hgt'][:-2]) < 150 or int(td['hgt'][:-2]) > 193:
                    print("Failed hgt test - cm")
                    # rejected_list.append(td)
                    continue
            if td['hgt'][-2:] == 'in':
                if int(td['hgt'][:-2]) < 59 or int(td['hgt'][:-2]) > 76:
                    print("Failed hgt test - in")
                    # rejected_list.append(td)
                    continue
            # the case that it's neither 'in' or 'cm'
            if td['hgt'][-2:] != 'in' and td['hgt'][-2:] != 'cm':
                print("Failed hgt test - unit type")
                # rejected_list.append(td)
                continue
            # Hex color pattern
            pattern = '^#[a-f0-9]{6}'
            if not re.match(pattern, str(td['hcl'])):
                print("Failed hcl test")
                # rejected_list.append(td)
                continue
            if td['ecl'] not in eyc_list:
                print("Failed ecl test")
                # rejected_list.append(td)
                continue
            # pid pattern 9 digits including 0's
            pattern = '[0-9]{9}'
            if not re.match(pattern, str(td['pid'])):
                print("Failed pid test")
                rejected_list.append(td)
                continue

            accepted_list.append(kv_pairs)
        else:
            print('PT 1 -- FAIL')
    
    print("accepted:", len(accepted_list))
    print("rejected:", len(rejected_list))
    
    # # Debug:
    # print("\n////////// ITEMS ACCEPTED ////////")
    # print(accepted_list)