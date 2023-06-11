import os
import sys

from typing import List

from helpers.validation import validate_file_input


def get_calories_list(input_file: str) -> List[int]:
    total_calories_per_elf = [0]

    try:
        with open(input_file, "r") as f:
            for line in f:
                line = line.strip()

                if len(line) == 0:
                    total_calories_per_elf.append(0)
                else:
                    total_calories_per_elf[-1] += int(line)

        return total_calories_per_elf
    except FileNotFoundError as err:
        print(f"Could not find specified file: {input_file}")
        sys.exit(1)


def get_top_3(calories: List[int]) -> List[int]:
    if len(calories) < 3:
        raise ValueError(
            f"expected list with at least 3 elements, received {calories}")

    top_3 = [0, 0, 0]

    for c in calories:
        if c > top_3[0]:
            top_3[0] = c
            top_3.sort()

    return top_3


if __name__ == "__main__":
    validate_file_input(sys.argv)

    input_file = sys.argv[1]

    calories = get_calories_list(input_file)
    print(calories)

    print(f"max calories: {max(calories)}")

    top_3_calories = get_top_3(calories)
    print(f"top_3: {top_3_calories}")
    print(f"top_3 total: {sum(top_3_calories)}")
