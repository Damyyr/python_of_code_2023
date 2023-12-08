def part1():
    with open('input.txt', 'r') as file:
        total_points = 0
        for game in file:
            parsed_game = game.split(": ", 1)[1].strip().split("|")
            winning_numbers = list(map(int, parsed_game[0].split()))
            numbers_obtained = list(map(int, parsed_game[1].split()))
            matches = len(set(winning_numbers) & set(numbers_obtained))
            if matches > 0:
                total_points += pow(2, matches - 1)

        print("Part 1 : " + str(total_points))

def part2():
    with open('input.txt', 'r') as file:
        games = [game.split(": ", 1)[1].strip().split("|") for game in file]
        game_counts = [1] * len(games)
        total_cards = len(games)
        i = 0
        while i < total_cards:
            winning_numbers = list(map(int, games[i][0].split()))
            numbers_obtained = list(map(int, games[i][1].split()))
            matches = len(set(winning_numbers) & set(numbers_obtained))
            if matches > 0 and i < total_cards - 1:
                for j in range(i+1, min(i+1+matches, total_cards)):
                    game_counts[j] += game_counts[i]
            i += 1
        total_cards = sum(game_counts)
        print("Part 2 : " + str(total_cards))

part1()
part2()