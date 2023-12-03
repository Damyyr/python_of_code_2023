import importlib, re
inputs = importlib.import_module('input-damyyr')

# The fuck is numpy, yo
def multiply_array(arr):
  r = 1
  for x in arr:
    r = x * r
  
  return r

def is_possible(loadout):
  draws = re.split(';', loadout)

  for draw in draws:
    balls = re.findall('(\d+.\w+)', draw)

    available_red = 12
    available_green = 13
    available_blue = 14

    for ball in balls:
      color = re.search('\w+$', ball).group(0)
      taken = int(re.search('\d+', ball).group(0))

      match color:
        case 'red': available_red -= taken
        case 'green': available_green -= taken
        case 'blue': available_blue -= taken

      for result in [available_red, available_green ,available_blue]:
        if result < 0: return False
      

  return True

def power_of(loadout):
  draws = re.split(';', loadout)

  red = 0
  green = 0
  blue = 0

  for draw in draws:
    balls = re.findall('(\d+.\w+)', draw)

    for ball in balls:
      color = re.search('\w+$', ball).group(0)
      showed = int(re.search('\d+', ball).group(0))
      # print('{} taken from {}'.format(taken, color))

      match color:
        case 'red': red = showed if showed >= red else red
        case 'green': green = showed if showed >= green else green
        case 'blue': blue = showed if showed >= blue else blue

  return multiply_array([red, green, blue])

games = []

# Chal 1
# for game in inputs.PROD:
#   id = int(re.search('\d+', game).group(0)) # `search()` will only math the first occurence
#   loadout = re.split(':', game)[1]
#   possible = is_possible(loadout)
#   
#   print('Game {}: {}'.format(id, possible))
#
#   if possible: games.append(id)

# Chal 2
for game in inputs.PROD:
  id = int(re.search('\d+', game).group(0)) # `search()` will only math the first occurence
  loadout = re.split(':', game)[1]

  games.append(power_of(loadout))

# Results
print('Result: {}'.format(sum(games)))