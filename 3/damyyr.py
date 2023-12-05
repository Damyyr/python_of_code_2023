import importlib, re
inputs = importlib.import_module('input-damyyr')

SYMBOL_MATCHER = '[^a-zA-Z0-9\.]'
GEAR_MATCHER = '\*'

# Create a 2D array with a default value
def create_and_populate(nb_line, nb_col, value):
  print('Creating an array {}x{}'.format(nb_col, nb_line))
  arr = []
  # Populate with 0s. Note that `[ [0] * nb_col] * nb_line` is a terrible idea as the same array will be referenced on each lines
  for l in range(nb_line):
    arr.insert(l, [])
    for c in range(nb_col):
      arr[l].insert(c, value)

  return arr

# This will add `1`s around the selected spot and a + 1 on the center (think minesweaper)
# This WILL modify the passwd array
def pin_symbol(line, col, array):
  # print('Pin added on {}x{}'.format(line, col)) # Debug
  array[line][col] = 1

  for il in range(line-1, line+2):
    for ic in range(col-1, col+2):
      array[il][ic] += 1

# This will pin the desired pin around the selected spot
# This WILL modify the passwd array
def pin_gear(line, col, value, array):
  # print('Pin added on {}x{}'.format(line, col)) # Debug

  for il in range(line-1, line+2):
    for ic in range(col-1, col+2):
      if array[il][ic] == 0: array[il][ic] = value

def pretty_print(array):
  # Fancy method found on the web
  for _ in array:
    for i in _:
        print(i, end=" ")
    print()
  # Method me
  # for i in range(len(array)):
  #   print(array[i])

# ---- main
considered_input = inputs.PROD

places = create_and_populate(len(considered_input), len(considered_input[0]), 0)

# Chal 1 | 521601
# for line_idx, line in enumerate(considered_input):
#   for col_idx, col in enumerate(line):
#     if re.match(SYMBOL_MATCHER, col): pin_symbol(line_idx, col_idx, places)
#
#
# taken = []
# for idx, row in enumerate(considered_input):
#   for matched in re.finditer('\d+', row):
#     if places[idx][matched.start()] > 0 or places[idx][matched.end()-1] > 0:
#       # print('{} should be taken in account'.format(matched.group(0))) # Debug
#       taken.append(int(matched.group(0)))
#     else:
#       []
#       # print('{} should NOT be taken in account'.format(matched.group(0))) # Debug

# print('Result Chal 1: {}'.format(sum(taken)))


# Chal 2 | 80694070
idx_pin = 0
for line_idx, line in enumerate(considered_input):
  for col_idx, col in enumerate(line):
    idx_pin += 1
    if re.match(GEAR_MATCHER, col): pin_gear(line_idx, col_idx, idx_pin, places)

dic = dict()

for idx, row in enumerate(considered_input):
  for matched in re.finditer('\d+', row):
    if places[idx][matched.start()] > 0 or places[idx][matched.end()-1] > 0:
      # Find the current indice my checking the max value in the neighbourhood (to find only one to match)
      pp = []
      for i in range(matched.start(), matched.end()):
        pp.append(places[idx][i])
      max_val = max(pp)

      # Check for the max value
      if max_val in dic: 
        dic[max_val].append(int(matched.group(0)))
      else:
        # If not already in the dict, it should be added as it's the first time we see a number for this indice
        dic[max_val] = [int(matched.group(0))]

pre_sum = []
# Compile data by checking only gear with 2 numbers
for gear_id, values in dic.items():
  if len(values) != 2: continue

  pre_sum.append(values[0]*values[1])

print('Result Chal 2: {}'.format(sum(pre_sum)))