import os

from rucksack_packing import load_rucksack_data, get_overlapping_items_in_comparments, get_overlapping_item_priority, \
    get_sum_of_priorities, find_overlapping_item_in_group, get_overlapping_item_priority_in_group, get_sum_of_group_priorities, \
    get_rucksack_groups

rucksacks_data = [
    "vJrwpWtwJgWrhcsFMMfFFhFp",
    "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
    "PmmdzqPrVvPwwTWBwg",
    "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
    "ttgJtRGJQctTZtZT",
    "CrZsJsPPZsGzwwsLwLmpwMDw"
]


def test_load_rucksack_data():
    dir_path = os.path.dirname(os.path.relpath(__file__))
    file_path = os.path.join(dir_path, "test_rucksack_data.txt")

    rucksacks = load_rucksack_data(file_path)

    assert rucksacks_data == rucksacks


def test_get_rucksack_groups():
    groups = get_rucksack_groups(rucksacks_data)

    assert groups == [
        [
            "vJrwpWtwJgWrhcsFMMfFFhFp",
            "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
            "PmmdzqPrVvPwwTWBwg"
        ],
        [
            "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
            "ttgJtRGJQctTZtZT",
            "CrZsJsPPZsGzwwsLwLmpwMDw"
        ]
    ]


def test_get_overlapping_items_in_comparments():
    expected_items = ["p", "L", "P", "v", "t", "s"]
    overlapping_items = []

    for r in rucksacks_data:
        overlapping_items.append(get_overlapping_items_in_comparments(r))

    for expected_item, overlapping_item in zip(expected_items, overlapping_items):
        assert expected_item == overlapping_item


def test_get_overlapping_item_priority():
    expected_priorities = [16, 38, 42, 22, 20, 19]

    priorities = []

    for r in rucksacks_data:
        priorities.append(get_overlapping_item_priority(r))

    for expected_priority, priority in zip(expected_priorities, priorities):
        assert expected_priority == priority


def test_get_sum_of_priorities():
    assert get_sum_of_priorities(rucksacks_data) == 157


def test_find_overlapping_item_in_group():
    g1 = [
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg"
    ]

    g2 = [
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw"
    ]

    assert find_overlapping_item_in_group(g1) == "r"
    assert find_overlapping_item_in_group(g2) == "Z"


def test_get_overlapping_item_priority_in_group():
    g1 = [
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg"
    ]

    g2 = [
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw"
    ]

    assert get_overlapping_item_priority_in_group(g1) == 18
    assert get_overlapping_item_priority_in_group(g2) == 52


def test_get_sum_of_group_priorities():
    assert get_sum_of_group_priorities(rucksacks_data) == 70
