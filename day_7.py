"""
Three major steps in Part 1:
First is mapping out all the nodes,
Second is to identify all 'starting nodes' AKA where a shiny gold bag is mentioned
Third is then seeing how many CONNECTIONS between shiny gold bag and UNIQUE other bags
"""
"""
For Part 2:
the output of interest is now different, looking to create a series of nested lists
ie: [2,1,3,[2,3,1,4,[2,1]]] where the number preceding a nested list will be multiplied
by the sum of its interiors and so on (recursive approach to 'flattening' it)
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
      conn_capacities = [capacity for capacity in nodes[loc].values()]
      debug_log.append(conn_capacities)
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

def all_subs(nodes, starting_locs, output=[]):
  """For Part 2, count each of the bags the shiny gold bag holds.
  the recursive component now acts upon when it reaches the final node of a branch
  """
  # Start from each departure
  for loc in starting_locs:
    # Create list of all sub-nodes' names (or bags) for this loc
    try:
      subs = [node for node in nodes[loc].keys()]
    except KeyError: # 'contains no other bags'
      subs = [] 
    debug_log.append(loc)
    debug_log.append(subs)
    # If there are sub-nodes, keep going deeper
    if len(subs) > 0: 
      # get the capacities for each sub-node
      conn_capacities = [int(capacity) for capacity in nodes[loc].values()]
      debug_log.append(conn_capacities)
      # get the idx of where to insert the nested array
      pos = starting_locs.index(loc) + 1
      # establish the nested array by going deeper
      output.append(conn_capacities)
      output = all_subs(nodes, subs, output)

    # reached the end of a branch - shouldn't go deeper
    else:
      debug_log.append("no further subs for:"+loc)
  
  return output

print("\n")
with open("day_7_inputs.txt", 'r') as f:
  nodes = {}
  # Example of each node in nodes
  # node_color: {
  #   inc_color: inc_cap,
  #   inc_color: inc_cap,
  #   inc_color: inc_cap,
  # }
  starting_nodes = []
  dead_ends = []
  

  for line in f:
    # Find all the nodes in which a shiny gold bag can be carried in
    # Sentence structures are 3 Total:

    # No connection - add to nodes
    if line.count('no other bags') > 0:
      node_color = line[:line.find('bag')-2] # first instance of 'bag'
      dead_ends.append(node_color)
      nodes[node_color] = {}

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
    
  # results = all_paths(nodes, starting_nodes)
  # remove duplicates
  # print(results)
  # print(len(results)) #376 not checked for unique
  # print(len(set(results))) #370 correct

  def algo_b(loc, output=[]):
    debug_log.append(loc)

    try:
      sub_nodes = [node for node in nodes[loc].keys()] 
      sub_node_caps = [val for val in nodes[loc].values()]
      debug_log.append(sub_nodes)
      debug_log.append(sub_node_caps)
    except KeyError:
      sub_nodes = []
    if len(sub_nodes) > 0:
      for n in sub_nodes:
        output.append(int(nodes[loc][n]))
        temp = algo_b(n)
      
        output.append(temp)
    debug_log.append(output)
    return output

  results_b = algo_b('shiny gold')
  print(results_b)

  with open('day_7_debug.txt', 'r') as dbug:
    for i in debug_log:
      dbug.writelines(str(i))
  