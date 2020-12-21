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
    


    for elem in data:
        kv_pairs = elem.split(" ")
        print(kv_pairs)

        # Just want the keys - seperate them:
        keys = [segment.split(":")[0] for segment in kv_pairs]
        print(keys)

        # using list comprehension
        check = [True if field in keys else False for field in req_fields] 
        print(check)
        if all(check):
            accepted_list.append(kv_pairs)            
        
    print(len(accepted_list))
