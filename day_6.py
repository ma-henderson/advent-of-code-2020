with open('day_6_inputs.txt', 'r') as f:
    

    # Step 1) Data Collection
    groups = []
    temp = []
    prev_char = "\n"
    for line in f:
        for char in line:
            # Means we have a new group
            if prev_char == "\n" and char == "\n":
                # Group's members seperated by a " "
                groups.append(" ".join(temp))
                temp = []
            # Put all members' answers together
            elif char == '\n' and prev_char != '\n' and prev_char != ' ':
                temp.append(line[:-1])
            
            prev_char = char

    # print(groups)

    # Step 2) Data cleaning (remove dupes)
    uniques = []
    for group in groups:
        # print("\n")
        group = sorted(group)
        # print("".join(group))
        group = set("".join(group))
        
        # print("".join(sorted(group)))
        uniques.append("".join(sorted(group)))
    
    # Step 3) Count
    the_sum = 0
    for item in uniques:
        the_sum += len(item.strip())
    print(the_sum)




    
    
