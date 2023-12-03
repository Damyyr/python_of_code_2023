import importlib, re
inputs = importlib.import_module('input-damyyr')

def to_int_list(array):
  return list(map(lambda x: int(x), array))

def to_str_list(array):
  return list(map(lambda x: str(x), array))

def extract_number(str):
  results = re.findall(r'\d+', str)
  results = ''.join(results)

  numbers = [results[0], results[len(results)-1]]

  # Debug
  # print('result>>{}<<'.format(results))
  # print('numbers>>{}<<'.format(numbers))

  return int(''.join(numbers))

def extract_number2(str):
  # Could also have worked with two arrays && zip function
  digits = dict({ 
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
  })

  # Sorted by design
  returns = dict()

  for digit, value in digits.items():
    # Find all occurence of each keys
    for match in re.finditer(digit, str):
      returns[match.start()] = value
      # returns.append({'digit': value, 'index': match.start()})

  # Sort data per index and transform it to a list (to get the first and last)
  sorted_returns = list(dict(sorted(returns.items())).values())

  # Debug
  # print('all: {} | first: {} || last: {}'.format(sorted_returns, sorted_returns[0], sorted_returns[-1]))

  # Returns first and last
  return [sorted_returns[0], sorted_returns[-1]]

# --------------

numbers = []

# Chal 1
# for line in inputs.PROD:
#   extracted = extract_number(line)
#   print('from: {} | extracted: {}'.format(line, extracted))
#   numbers.append(extracted)

# Chal 2
for line in inputs.PROD:
  extracted = extract_number2(line)
  extracted = ''.join(to_str_list(extracted))
  print('from: {} | extracted: {}'.format(line, extracted))
  numbers.append(int(extracted))


# Result
print('result: {}'.format(sum(numbers)))