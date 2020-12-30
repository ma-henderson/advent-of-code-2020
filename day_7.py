"""
Three major steps in Part 1:
First is mapping out all the nodes,
Second is to identify all 'starting nodes' AKA where a shiny gold bag is mentioned
Third is then seeing how many CONNECTIONS between shiny gold bag and UNIQUE other bags
"""


with open("day_7_inputs", 'r') as f:
  nodes = {}
  # node_color: {
  #   inc_color: inc_cap,
  #   inc_color: inc_cap,
  #   inc_color: inc_cap,
  # }

  for line in f:
    # Find all the nodes in which a shiny gold bag can be carried in

    # Sentence structures are 3 Total:
    # No connection
    if line.count('no other bags') > 0:
      print()
      # ignore?

    # Direct (without commas)
    elif line.count(",") == 0:
      # 1) Node color
      node_color = line[:line.find('bag')-2] # first instance of 'bag'

      # 2) Incoming Capacity (for that color)
      num_loc = line.find('contain')+8
      inc_cap = line[num_loc]

      # 3) Incoming color
      inc_color_temp = line[num_loc+2:]
      inc_color_end = inc_color_temp.find('bag') - 2
      inc_color = inc_color_temp[:inc_color_end]
      
      # instantiate this node-inc connection as a dict
      nodes[node_color][inc_color] = inc_cap
    

    # striped tan bags contain 5 mirrored olive bags, 4 dark maroon bags.
    # Connection (with commas -> no 'and' to look out for)
    elif line.count(',') > 0:
      # 1) Node Color

      # 2) Loop per ,
      # 2.1) Inc Capacity

      # 2.2) Inc Color

      # 2.3) Register data into nodes