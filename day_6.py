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

    print(groups[:5])

    # Step 2) Data cleaning (remove dupes)
    uniques = []
    the_sum = 0
    for group in groups:
        # print("\n")

        # How many people in this group:
        group_count = 1
        group_count += len([" " for reply in group if reply == " "])
        # print(group_count)

        # All replies prepared for set()
        # In order: ABC sort, join sorted list, strip whitespaces
        group = "".join(sorted(group)).strip()
        # print(group)

        # Get only uniques
        group_temp = set(group)
        # print("".join(sorted(group_temp)).strip())
        
        # Keep only answers to which ALL have answerd YES to:
        all_count = len([True for reply in group_temp if group.count(reply) == group_count])
        # print(all_count)

        the_sum += all_count


    
    print(the_sum)
