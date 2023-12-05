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
    print("Part 2 : Not Done 🥲")
    # TODO: finish this
    # inventory = {}
    # card_counter = 1 # i guess its a counter, could have named this deck_index or somth idk
    # with open('input.txt', 'r') as file:
    #     for game in file:
    #         parsed_game = game.split(": ", 1)[1].strip().split("|")
    #         winning_numbers = list(map(int, parsed_game[0].split()))
    #         numbers_obtained = list(map(int, parsed_game[1].split()))
    #         matches = len(set(winning_numbers) & set(numbers_obtained))
    #         next = [i for i in range(card_counter + 1, card_counter + matches + 1)]
    #         card_counter += 1
    #         print(next)



part1()
part2()