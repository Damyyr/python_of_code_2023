import re

# AY AY, WE SAID FUCK NUMPYYY
def multiply_list(lst):
    result = 1
    for num in lst:
        result *= num
    return result

def prep_data():
    file = open('input.txt')
    board = []
    for line in file:
        board.append(line)
    file.close()
    chars = {}
    for r in range(140):
        for c in range(140):
            if r < len(board) and c < len(board[r]) and board[r][c] not in '01234566789.': # dont look at this
                chars[(r, c)] = []
    r = 0
    while r < len(board):
        row = board[r]
        for n in re.finditer(r'\d+', row):
            edge = set()
            for r2 in range(r-1, r+2):
                for c in range(n.start()-1, n.end()+1):
                    edge.add((r2, c))
            for o in edge:
                if o in chars.keys():
                    chars[o].append(int(n.group()))
        r += 1
    return chars

chars = prep_data()
sum_of_sums = 0
for p in chars.values():
    sum_of_sums += sum(p)
sum_of_products = 0
for p in chars.values():
    if len(p) == 2:
        sum_of_products += multiply_list(p)

print('Part 1 : ' + str(sum_of_sums))
print('Part 2 : ' + str(sum_of_products))