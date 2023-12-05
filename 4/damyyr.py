import importlib, re
inputs = importlib.import_module('input-damyyr')

# Returns, in order: id, winnings, draw
def parse_card(card):
  card_info, numbers = card.split(': ')
  id = re.search("\d+", card_info).group(0)
  winnings, draw = numbers.split(' | ')
  draw = re.findall('\d+', draw)
  winnings = re.findall('\d+', winnings)

  return [id, winnings, draw]

considered_input = inputs.PROD

results = dict()

# Chal 1 | 23847
# for card in considered_input:
#   id, winnings, draw = parse_card(card)
#
#   card_value = 0
#   for number in draw:
#     if number in winnings:
#       print('{}: {} in {}! Doubling {}'.format(id, number, winnings, card_value))
#       card_value = 1 if card_value == 0 else card_value * 2
#
#   results[id] = card_value

# ---------------------------------------------------------------------------------

# Chal 2 | 8570000

def add_to_cards(id, multiplier):
  if id in results:
    results[id] += multiplier
  else:
    results[id] = multiplier

def process(card, factor=1):
  id, _, _ = parse_card(card)

  print('Winning card {} (x{})'.format(id, factor))
  add_to_cards(id, factor)

for idx, card in enumerate(considered_input):
  id, winnings, draw = parse_card(card)

  results[id] = results[id] + 1 if id in results else 1
  next_factor = results[id] if id in results else 1

  to_check = idx + 1
  for number in draw:
    if number in winnings:
      process(considered_input[to_check], next_factor)
      to_check += 1

print(results)
print(sum(results.values()))