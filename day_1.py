inputs = [1078,1109,1702,1293,1541,1422,1679,1891,1898,1455,1540,1205,1971,1582,1139,1438,1457,1725,1907,1872,1101,1403,1557,1597,1619,1974,1287,292,1647,1444,1241,879,1761,1067,1178,1510,1110,1233,1121,1299,1796,1124,1768,1466,1871,1279,1344,1485,1258,1179,1147,492,1234,1843,1421,1819,1964,1671,1793,1302,1731,1886,1686,1150,1806,1960,1841,1936,1845,1520,1779,1102,1323,1892,1742,1941,1395,1525,1165,715,1829,1448,1906,1191,1981,1115,1716,1644,1310,1836,1105,1517,1790,1950,1741,1256,1467,1677,1372,1838,1637,1143,1763,1222,1291,1835,1602,1927,1933,1952,1692,1662,1967,1791,1984,1176,1324,1460,1416,562,1862,1273,1518,1535,1093,1977,1923,1246,1570,1674,1861,1811,1431,47,1158,1912,1322,1062,1407,1528,1068,1868,1997,1930,959,1676,1759,2000,1993,1722,1738,1264,1361,1542,1187,1735,1405,1745,1753,1833,1493,1311,1547,1180,1553,1513,1812,1951,1948,1834,1925,1726,1326,1931,1962,1947,1173,1633,1901,1781,1483,1789,1417,1929,1859,1760,1347,1996,1328,1798,1230,1298,1877,1840,1607,1253,1057,1650,1171,1593]

def twoto2020(values):
  # Sort code Largest to Smallest
  new_values = sorted(values, reverse=True)
  # remove duplicates? only if not 1010 (2020/2)

  # Take top value and add it to bottom value until sum > 2020
  i = -1
  for val in new_values:
    # once the sum is 2020:
    if val + new_values[i] == 2020:
      # Multiply them together, return the answer
      return val * new_values[i]
    
    # Once > 2020, Go down a peg from top value
    elif val + new_values[i] > 2020:
      continue
    
    # still doesn't add up to (or more than) 2020, next bottom val
    elif val + new_values[i] < 2020:
      i -= 1

answer_1 = twoto2020(inputs)
print(answer_1)

def threeto2020(values):
  # eliminate impossible inputs: max + sum(2mins) < 2020
  new_values = sorted(values, reverse=True)
  data_values_removed = []

  for val in new_values:
    max_val = new_values[0]
    if max_val + new_values[-1] + new_values[-2] > 2020:
      data_values_removed.append(new_values.pop(0))
    else:
      break
  
  print(len(data_values_removed), new_values)

  # Working from lowest combo to highest
  i = -2
  pivots = []

  pivots.append(new_values[0])
  #the inner-most loop will be the middle value
  pivots.append(new_values[i])
  pivots.append(new_values[-1])
  

  # Check if the sum is < 2020
  for i in range(-2,(len(new_values)-2)*-1, -1):
    if sum(pivots) == 2020:
      return pivots
    elif sum(pivots) < 2020:
      continue
    elif sum(pivots) > 2020:
      # bring the top peg down
      continue


def threeto2020(values):
  # eliminate impossible inputs: max + sum(2mins) < 2020
  new_values = sorted(values, reverse=True)
  data_values_removed = []

  for val in new_values:
    max_val = new_values[0]
    if max_val + new_values[-1] + new_values[-2] > 2020:
      data_values_removed.append(new_values.pop(0))
    else:
      break