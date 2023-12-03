def parse_cubes(round):
    cubes = {'red': 0, 'green': 0, 'blue': 0}
    for cube in round.split(', '):
        num, color = cube.split(' ')
        cubes[color] = max(cubes[color], int(num))
    return cubes

def part1():
    possible_games = []
    with open('input.txt', 'r') as file:
        for game in file:
            game_id, game_info = game.strip().split(': ')
            game_id = int(game_id.split(' ')[1])
            rounds = game_info.split('; ')
            cubes = {'red': 12, 'green': 13, 'blue': 14}
            if all(parse_cubes(round)[color] <= cubes[color] for round in rounds for color in cubes):
                possible_games.append(game_id)
    print("Part 1 : " + str(sum(possible_games)))

def part2():
    total_power = 0
    with open('input.txt', 'r') as file:
        for game in file:
            game_info = game.strip().split(': ')[1]
            rounds = game_info.split('; ')
            cubes = {color: max(parse_cubes(round)[color] for round in rounds) for color in ['red', 'green', 'blue']}
            total_power += cubes['red'] * cubes['green'] * cubes['blue']
    print("Part 2 : " + str(total_power))

part1()
part2()