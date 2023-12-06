import math 
"""
  T  - r as race time
  B  - c as charge time
  t  - m as movement time
    => r = m + c 
    1 => m = r - c

  D  - d as final distance
    2 => d = m * c

  1 in 2 => d = (r - c) * c 
  => d = rc - c^2
  => c^2 - rc + d = 0 

  solutions:
  c1 = (r + SQRT(r^2 - 4 * d))/2
  c2 = (r - SQRT(r^2 - 4 * d))/2

"""
def get_content(filename: str) -> list[str]:
    with open(filename, "r") as file:
        content = file.read().split('\n')
    return content


def day06part1(filename: str) -> int:
    data = get_content(filename)
    races = [int(value) for value in data[0].replace("Time:", "").strip().split(" ") if value != '']
    distances = [int(value) for value in data[1].replace("Distance:", "").strip().split(" ") if value != '']

    solution = 1
    for i in range(len(races)):
        r = races[i]
        d = distances[i]
        print(f"r=${r} d=${d}")
        delta = math.sqrt(pow(r, 2) - 4 * d)
        c1 = math.ceil((r + delta)/2)
        c2 = math.floor((r - delta)/2)
        print(f"c1=${c1} c2=${c2}")
        race_solution = c1 - c2 - 1
        print(race_solution)
        solution *= race_solution
    return solution

if __name__ == "__main__":
    test_result = day06part1("input-files/day06part1.test")
    print(test_result)
    assert test_result == 288

    test_result = day06part1("input-files/day06part1.input")
    print(test_result)
    assert test_result == 3316275