import os
import sys
import string

from typing import List

from helpers.validation import validate_file_input, handle_file_not_found

PRIORITY_MAPPING = dict()

for c, priority in zip(string.ascii_lowercase, range(1, 27)):
    PRIORITY_MAPPING[c] = priority
for c, priority in zip(string.ascii_uppercase, range(27, 53)):
    PRIORITY_MAPPING[c] = priority


def load_rucksack_data(file_path: str) -> List[str]:
    rucksacks = []

    try:
        with open(file_path, "r") as f:
            for line in f:
                line = line.strip()
                rucksacks.append(line)

            return rucksacks
    except FileNotFoundError as err:
        handle_file_not_found(file_path)


def get_rucksack_groups(rucksacks: List[str]) -> List[List[str]]:
    """
    split rucksacks into gruops of 3
    """

    counter = 0
    group = []
    groups = []

    for r in rucksacks:
        counter += 1
        group.append(r)

        if counter == 3:
            groups.append(group)
            group = []
            counter = 0

    return groups


def find_overlapping_item_in_group(rucksacks: List[str]) -> str:
    return set.intersection(*[set(r) for r in rucksacks]).pop()


def get_overlapping_items_in_comparments(rucksack: str) -> str:
    """
    Rucksack is represented as a string, where each character corresponds to an item.
    There are two compartments in a rucksack, first half of the string represents the frist compartment,
    the second half of the string represents the second compartment.
    Overlapping item is an item that is found in both compartments.
    We expect that each rucksack has one overlapping item.
    """

    middle = len(rucksack) // 2
    first_compartment = set(rucksack[:middle])
    second_compartment = set(rucksack[middle:])
    overlapping_items = set.intersection(first_compartment, second_compartment)
    return overlapping_items.pop()


def get_overlapping_item_priority(rucksack: str) -> int:
    overlapping_item = get_overlapping_items_in_comparments(rucksack)
    return PRIORITY_MAPPING.get(overlapping_item)


def get_overlapping_item_priority_in_group(rucksack_group: List[str]) -> int:
    overlapping_item = find_overlapping_item_in_group(rucksack_group)
    return PRIORITY_MAPPING.get(overlapping_item)


def get_sum_of_priorities(rucksacks: List[str]) -> int:
    priorities_sum = 0

    for r in rucksacks:
        priorities_sum += get_overlapping_item_priority(r)

    return priorities_sum


def get_sum_of_group_priorities(rucksacks: List[str]) -> int:
    priorities_sum = 0
    rucksack_groups = get_rucksack_groups(rucksacks)

    for group in rucksack_groups:
        priorities_sum += get_overlapping_item_priority_in_group(group)

    return priorities_sum


if __name__ == "__main__":
    validate_file_input(sys.argv)

    input_file = sys.argv[1]
    rucksacks = load_rucksack_data(input_file)

    print(f"priorities sum: {get_sum_of_priorities(rucksacks)}")

    print(f"group priorities sum: {get_sum_of_group_priorities(rucksacks)}")
