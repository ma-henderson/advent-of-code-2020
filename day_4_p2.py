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
                temp.append(line[:-2]) #[:-2] avoids taking \n with it
            prev_char = char
        counter += 1
    


    for elem in data[:3]:
        # turn string into list of kv-pairs
        kv_pairs = elem.split(" ")
        print(kv_pairs)

        # //// Part 2 //// 
        # Creating a dictionary
        keys = [segment.split(":")[0] for segment in kv_pairs]
        values = [segment.split(":")[1] for segment in kv_pairs]
        td = {}
        print(keys)
        print(values)

        for i in range(len(kv_pairs)):
            td[keys[i]] = [values[i]]   
        
        # print(td)

        flag = True
        while flag == True:
            # contains all required fields? (PART 1)
            if all([True if field in keys else False for field in req_fields]):
                accepted_list.append(kv_pairs)

                # required fields in correct format? (PART 2)
                if len(td['byr']) != 4 or td['byr'] < 1920 or td['byr'] > 2002:    
                    flag = False
                if len(td['iyr']) != 4 or td['iyr'] < 2010 or td['byr'] > 2020:    
                    flag = False
                if len(td['eyr']) != 4 or td['iyr'] < 2020 or td['byr'] > 2030:    
                    flag = False
                if td['hgt'][-2:] == 'cm':
                    if td['hgt'][:-2] < 150 or td['hgt'][:-2] > 193:
                        flag = False
                if td['hgt'][-2:] == 'in':
                    if td['hgt'][:-2] < 59 or td['hgt'][:-2] > 76:
                        flag = False
                # the case that it's neither 'in' or 'cm'
                if td['hgt'][-2:] != 'in' and td['hgt'][-2:] != 'cm':
                    flag = False
                # Hex color pattern
                pattern = '^#[a-f0-9]{6}'
                if not re.match(pattern, str(td['hcl'])):
                    flag = False
                if td['ecl'] not in eyc_list:
                    flag = False
                # pid pattern 9 digits including 0's
                pattern = '[0-9]{9}'
                if not re.match(pattern, str(td['pid'])):
                    flag = False
                # ...
                accepted_list.append(kv_pairs)
            flag = False
    # print(len(accepted_list))
    print(accepted_list)