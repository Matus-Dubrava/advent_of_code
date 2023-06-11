import os
import pytest

from calories import get_calories_list, get_top_3


def test_get_calories():
    dir_path = os.path.dirname(os.path.relpath(__file__))
    input_file = os.path.join(dir_path, "test_data.txt")

    calories = get_calories_list(input_file)
    expected_calories = [1, 6, 9, 1, 15, 4]
    assert calories == expected_calories


def test_get_top_3_calories():
    calories = [1, 6, 9, 1, 15, 4]
    top_3 = get_top_3(calories)
    assert top_3 == [6, 9, 15]


def test_get_top_3_calories_fail_when_not_enough_calories():
    invalid_calories_lists = [[], [1], [1, 1]]

    for calories in invalid_calories_lists:
        with pytest.raises(ValueError):
            get_top_3(calories)
