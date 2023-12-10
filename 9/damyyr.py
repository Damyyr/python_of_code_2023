import importlib
inputs = importlib.import_module('input-damyyr')

# Safeguard to avoid infinite loop
global count 
count = 0
LIMIT = 10000

considered_input = inputs.PROD

def gap(n1, n2):
  return n2 - n1

def all_is_0(numbers): return all([number == 0 for number in numbers])

def process_row(numbers, is_chal1 = True):
  global count
  count += 1
  if count >= LIMIT: return

  if all_is_0(numbers):
    return 0
  else:
    nb_gap = len(numbers) - 1

    new_row = []
    for i in range(nb_gap):
      if i % 2 != 0: next

      new_row.append(gap(numbers[i], numbers[i+1]))

    if is_chal1:
      return numbers[nb_gap] + process_row(new_row, is_chal1)
    else:
      return numbers[0] - process_row(new_row, is_chal1)
    

results = []

for idx, line in enumerate(considered_input):
  numbers = line.split(' ')
  numbers = [int(i) for i in numbers]

  # Chal 1 | 1762065988
  # result = process_row(numbers)

  # Chal2 | 1066
  result = process_row(numbers, False)

  print('Line #{}: {}'.format(idx, result))
  results.append(result)

print('Sum: {}'.format(sum(results)))
print('Done in {} "attempts"'.format(count))