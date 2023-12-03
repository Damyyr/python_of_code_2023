import re

#  man there's got to be a better way than this..
digit_map = {
    'zero': 'z0o',
    'one': 'o1e',
    'two': 't2o',
    'three': 't3e',
    'four': 'f4r',
    'five': 'f5e',
    'six': 's6x',
    'seven': 's7n',
    'eight': 'e8t',
    'nine': 'n9e'
}

def part1():
    with open('input.txt', 'r') as file:
        calibration_nb = 0
        for line in file:
            digits = re.findall(r'\d', line)
            calibration_nb += int(str(digits[0]) + str(digits[-1]))
    print("Part1 : " + str(calibration_nb))

def part2():
    with open('input.txt', 'r') as file:
        calibration_nb = 0
        for line in file:
            for word, digit in digit_map.items():
                line = line.replace(word, digit)
            digits = re.findall(r'\d', line)
            calibration_nb += int(str(digits[0]) + str(digits[-1]))
    print("Part2 : " + str(calibration_nb))
            
part1()
part2()