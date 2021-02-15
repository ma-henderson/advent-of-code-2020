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
  
  # Part 1)
  # for node in nodes:
  #   if any([True for color in nodes[node].keys() if color == "shiny gold"]):
  #     starting_nodes.append(node)
    
  # results = all_paths(nodes, starting_nodes)
  # remove duplicates
  # print(results)
  # print(len(results)) #376 not checked for unique
  # print(len(set(results))) #370 correct

  # Part 2)
  # 'global': nodes dictionary
  # inputs: name
  # outputs: sum
  def algo_c(name='shiny gold', the_sum=0):
    # Create list of subnodes' names (address) 
    sub_nodes = [node for node in nodes[name].keys()]
    # For each subnode in {nodes}:
    print(sub_nodes)
    for n in sub_nodes:
      print(name, n)
      # multiply its relevant qty by . . .
      # the sum of its recursive subnodes
      if n in nodes.keys():
        print(n, 'YES in nodes.keys()')
        print('adding', nodes[name][n], 'to sum and going deeper...')
        the_sum += int(nodes[name][n]) + int(nodes[name][n]) * algo_c(name=n)
      else:
        print(n, 'NOT in nodes.keys() adding', nodes[name][n], 'going to NEXT loop')
        the_sum += int(nodes[name][n])
    # return the sum
    print('returning sum of', the_sum, 'going UP a level...')
    return the_sum
  print(algo_c())
  
  #864 TOO LOW
  #557281663702534220544 too high
  #29547 correct, passing in the_sum per iteration was wrong
