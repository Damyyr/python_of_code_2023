defmodule Aoc23.Day02 do
  def solve(input, extract_number_fun) do
    input
    |> Enum.map(&extract_number_fun.(&1))
    |> Enum.sum()
  end


  def extract_game_id(<<"Game ", rest::binary>>) do
    rest
    |> String.split(":")
    |> List.first()
    |> String.to_integer()
  end

  def extract_max_per_color(str) do
    str
    |> String.split(":")
    |> List.last()
    |> String.split(~r/[,;]/, trim: true)
    |> Enum.map(&String.split(&1, ~r/\s+/, trim: true))
    |> Enum.reduce(%{}, fn [number_str, color], acc ->
        number = String.to_integer(number_str)
        Map.update(acc, color, number, &max(&1, number))
      end)
  end

  def possible_game(game, bag_of_dice) do
    %{ "blue" => b_hand, "red" => r_hand, "green" => g_hand } = game
    %{ "blue" => b_bag, "red" => r_bag, "green" => g_bag } = bag_of_dice
    b_hand <= b_bag and r_hand <= r_bag and g_hand <= g_bag
  end

  def exctract_possible_game_id(str) do
    id = with game <- extract_max_per_color(str),
         true <- possible_game(game, %{"red" => 12, "green" => 13, "blue" =>14})
         do
           extract_game_id(str)
         else
          _ -> 0
         end
    id
  end

  def extract_power_of_set(str) do
    str
    |> extract_max_per_color()
    |> Map.values()
    |> Enum.reduce(1, &(&1 * &2))
  end

end

alias Aoc23.Day02

input = File.stream!("input.txt")

input
|> Day02.solve(&Aoc23.Day02.exctract_possible_game_id/1)
|> IO.inspect(label: "Day02a")

input
|> Day02.solve(&Aoc23.Day02.extract_power_of_set/1)
|> IO.inspect(label: "Day02b")
