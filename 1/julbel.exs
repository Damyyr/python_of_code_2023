defmodule Aoc23.Day01 do
  def get_calibration_data(input, extract_number_fun) do
    input
    |> Enum.map(&extract_number_fun.(&1))
    |> Enum.sum()
  end

  def extract_number_part1(str) do
    digits =
      Regex.scan(~r/[[:digit:]]/, str)
      |> List.flatten()

    [List.first(digits), List.first(Enum.reverse(digits))]
    |> Enum.join()
    |> String.to_integer()
  end


  def extract_number_part2(str) do
    digits_spelled_regex = "one|two|three|four|five|six|seven|eight|nine|zero"
    first =
      Regex.run(~r/#{digits_spelled_regex}|[[:digit:]]/, str)
      |> List.first()
      |> to_digit()

    last =
      Regex.run(
        ~r/#{String.reverse(digits_spelled_regex)}|[[:digit:]]/,
        String.reverse(str)
      )
      |> List.first()
      |> String.reverse()
      |> to_digit()

    [first, last]
    |> Enum.join()
    |> String.to_integer()
  end

  digits_spelled = %{
    "one" => "1",
    "two" => "2",
    "three" => "3",
    "four" => "4",
    "five" => "5",
    "six" => "6",
    "seven" => "7",
    "eight" => "8",
    "nine" => "9"
  }

  for {spelling, digit} <- digits_spelled do
    defp to_digit(unquote(spelling) <> _), do: unquote(digit)
  end

  defp to_digit(digit), do: digit
end



  alias Aoc23.Day01

  input = File.stream!("input-julbel.txt")

    input
    |> Day01.get_calibration_data(&Aoc23.Day01.extract_number_part1/1)
    |> IO.inspect(label: "Day01a")

    input
    |> Day01.get_calibration_data(&Aoc23.Day01.extract_number_part2/1)
    |> IO.inspect(label: "Day01b")
