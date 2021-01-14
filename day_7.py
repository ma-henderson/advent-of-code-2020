"""
Three major steps in Part 1:
First is mapping out all the nodes,
Second is to identify all 'starting nodes' AKA where a shiny gold bag is mentioned
Third is then seeing how many CONNECTIONS between shiny gold bag and UNIQUE other bags
"""

# Major Step 3) Recursive check from starting nodes
debug_log = []
def all_paths(nodes, starting_locs, output=[]):  
  # Start from each departure
  for loc in starting_locs:
    # append current node to the output
    output.append(loc)
    connections = [node for node in nodes if loc in nodes[node].keys() and node not in output]
    # print(loc, connections)
    debug_log.append(loc)
    debug_log.append(connections)
    # Does each next destination link to another?
    if len(connections) > 0: 
      # True:
      # to avoid eternal loops: 
      # starting_locs.remove(loc)

      # call the fn itself once again
      output = all_paths(nodes, connections, output)
    else:
      # print("no further connections for:", loc)
      debug_log.append("no further connections for:"+loc)
      # False:
      # END the recursion (return the node)

  return output


print("\n")
with open("day_7_inputs.txt", 'r') as f:
  nodes = {}
  # node_color: {
  #   inc_color: inc_cap,
  #   inc_color: inc_cap,
  #   inc_color: inc_cap,
  # }
  starting_nodes = []
  dead_starts = []
  

  for line in f:
    # Find all the nodes in which a shiny gold bag can be carried in
    # Sentence structures are 3 Total:

    # No connection
    if line.count('no other bags') > 0:
      node_color = line[:line.find('bag')-2] # first instance of 'bag'
      dead_starts.append(node_color)

    # Direct (without commas)
    elif line.count(",") == 0:
      # 1) Node color
      node_color = line[:line.find('bag')-1] # first instance of 'bag'
      # 2) Incoming Capacity (for that color)
      num_loc = line.find('contain')+8
      inc_cap = line[num_loc]
      # 3) Incoming color
      inc_color_temp = line[num_loc+2:]
      inc_color_end = inc_color_temp.find('bag') - 1
      inc_color = inc_color_temp[:inc_color_end]
      # 4) Instantiate this node-inc connection as a dict
      # print(node_color, inc_color, inc_cap)
      try:
        nodes[node_color][inc_color] = inc_cap
      except KeyError: # doesn't already exist in nodes
        nodes[node_color] = {}
        nodes[node_color][inc_color] = inc_cap
    

    # Connection (with commas, no 'and' to look out for)
    elif line.count(',') > 0:
      # 1) Node Color
      node_color = line[:line.find('bag')-1] # first instance of 'bag'
      # 2) Loop per ,
      num_loc = line.find('contain') + 8
      for i in range(line.count(',') + 1):
        # 2.1) Inc Capacity
        inc_cap = line[num_loc]
        # 2.2) Inc Color
        inc_color_temp = line[num_loc+2:]
        inc_color_end = inc_color_temp.find('bag') - 1
        inc_color = inc_color_temp[:inc_color_end]
        # 2.3) Register data into nodes
        # print(node_color, inc_color, inc_cap)
        try:
          nodes[node_color][inc_color] = inc_cap
        except KeyError:
          nodes[node_color] = {}
          nodes[node_color][inc_color] = inc_cap

        num_loc = line.find(',',num_loc) + 2
  
  # MAJOR step 2)
  for node in nodes:
    if any([True for color in nodes[node].keys() if color == "shiny gold"]):
      starting_nodes.append(node)
    
  # for node in nodes:
  #   print("////", node, "////")
  #   for k,v in nodes[node].items():
  #     print('\t',k,v)
  print(starting_nodes)

  results = all_paths(nodes, starting_nodes)
  # remove duplicates
  print(results)
  print(len(results)) #376 not checked for unique
  print(len(set(results))) #370 correct

  with open('day_7_debug.txt', 'w') as deb:
    for line in debug_log:
      if type(line) == list:
        deb.write(",".join(line))
        deb.write("\n")
      else:
        deb.write(line)
        deb.write("\n")

