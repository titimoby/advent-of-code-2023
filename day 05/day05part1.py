import re


def get_content(filename: str) -> list[str]:
    with open(filename, "r") as file:
        content = file.read().split('\n\n')
    return content

def change_seed(seed, convert_maps):
  for converter in convert_maps:
    for i in range(0, len(converter), 3):
      dest, source, rng = converter[i:i + 3]
      if seed < source or seed > (source + rng - 1): 
        continue
      seed = seed - source + dest
      break
  return seed

def day05part1(filename: str) -> int:
    data = get_content(filename)
    values = [list(map(int, re.findall('\\d+', part))) for part in data]
    seeds, convert_maps = values[0], values[1:]
    # lowest possible float
    lowest_location = float('inf')

    for seed in seeds:
        seed = change_seed(seed, convert_maps)
        lowest_location = min(lowest_location, seed)
    return lowest_location

if __name__ == "__main__":
    test_result = day05part1("input-files/day05part1.test")
    assert test_result == 35
    print(test_result)
    test_result = day05part1("input-files/day05part1.input")
    assert test_result == 278755257
    print(test_result)