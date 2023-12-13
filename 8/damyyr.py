import importlib, re, itertools, time
# from array import *
inputs = importlib.import_module('input-damyyr')

# Safeguard to avoid infinite loop
global _count 
_count = 0
LIMIT = 100

# plus que 999999999

considered_input = inputs.PROD
directions = considered_input.pop(0)

ways = dict()

def index_way(to_index, ways):
  id, rest = to_index.split(' = ')
  rest = [i.group(0) for i in re.finditer('\w+', rest)]
  ways[id] = rest
  return

for way in considered_input:
  index_way(way, ways)


steps = 0

# Chal 1 | 12083
# index = 'AAA'
# while _count < LIMIT and index != 'ZZZ':
#   _count += 1
#   for direction in itertools.cycle(directions):
#     if index == 'ZZZ': break
#     if _count >= LIMIT: break
#     steps += 1
#     _count += 1

#     to_go = 0 if direction == 'L' else 1
#     index = ways[index][to_go]

# Chal2 | 13385272668829
def only_ending_by(way, end_by):
  if bool(re.search('..{}'.format(end_by), way)):
    return True
  
  return False

def only_ending_by_A(way): return only_ending_by(way, 'A')

def next_direction(current, directions):
  new_direction = current + 1
  return 0 if new_direction >= len(directions) else new_direction

# The return of non-usage of numpy
def multiply_array(arr):
  r = 1
  for x in arr:
    r = x * r
  
  return r

start_indexes = list(filter(only_ending_by_A, ways.keys()))

steps_by_index = dict()
all_indexes_idx = -1

while len(steps_by_index.keys()) != 6:
  steps = 0
  all_indexes_idx += 1
  index = start_indexes[all_indexes_idx]
  

  for direction in itertools.cycle(directions):
    to_go = 0 if direction == 'L' else 1

    if index[-1] == 'Z':
      print('{} found at steps {} ({} found)'.format(index, steps, len(steps_by_index.keys())))
      steps_by_index[index] = steps
      break

    steps += 1
    index = ways[index][to_go]