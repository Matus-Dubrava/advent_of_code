import os

from rock_paper_scissors import load_strategy_guide, get_outcome_points, compute_one_round_points, compute_total_points, \
    get_shape_based_on_wanted_outcome, get_shapes_based_on_wanted_outcome
from rock_paper_scissors_mappings import REVERSE_RESPONSE_MOVES_MAPPING, RPSMapping


def test_load_strategy_guide():
    dir_path = os.path.dirname(os.path.relpath(__file__))
    file_path = os.path.join(dir_path, "./test_rps_data.txt")

    oponent_moves, responses = load_strategy_guide(file_path)

    assert oponent_moves == ['A', 'B', 'C']
    assert responses == ['Y', 'X', 'Z']


def test_get_outcome_points():
    oponent_moves = ['A', 'B', 'C']
    responses = ['Y', 'X', 'Z']

    expected_outcomes = [6, 0, 3]

    for oponent_move, response, expected_outcome in zip(oponent_moves, responses, expected_outcomes):
        assert get_outcome_points(oponent_move, response) == expected_outcome


def test_compute_one_round_points():
    oponent_moves = ['A', 'B', 'C']
    responses = ['Y', 'X', 'Z']

    expected_outcomes = [8, 1, 6]

    for oponent_move, response, expected_outcome in zip(oponent_moves, responses, expected_outcomes):
        assert compute_one_round_points(
            oponent_move, response) == expected_outcome


def test_compute_total_points():
    oponent_moves = ['A', 'B', 'C']
    responses = ['Y', 'X', 'Z']
    assert compute_total_points(oponent_moves, responses) == 15

    oponent_moves = ['A', 'B', 'C']
    wanted_outcomes = ['Y', 'X', 'Z']
    shapes_to_play = get_shapes_based_on_wanted_outcome(
        oponent_moves, wanted_outcomes)
    assert compute_total_points(oponent_moves, shapes_to_play) == 12


def test_get_shape_based_on_wanted_outcome():
    oponent_moves = ['A', 'B', 'C']
    wanted_outcomes = ['Y', 'X', 'Z']

    expected_shapes = [
        REVERSE_RESPONSE_MOVES_MAPPING.get(RPSMapping.rock),
        REVERSE_RESPONSE_MOVES_MAPPING.get(RPSMapping.rock),
        REVERSE_RESPONSE_MOVES_MAPPING.get(RPSMapping.rock)
    ]

    for oponent_move, wanted_outcome, expected_shape in zip(oponent_moves, wanted_outcomes, expected_shapes):
        assert get_shape_based_on_wanted_outcome(
            oponent_move, wanted_outcome) == expected_shape


def test_get_shapes_based_on_wanted_outcome():
    oponent_moves = ['A', 'B', 'C']
    wanted_outcomes = ['Y', 'X', 'Z']

    expected_shapes = [
        REVERSE_RESPONSE_MOVES_MAPPING.get(RPSMapping.rock),
        REVERSE_RESPONSE_MOVES_MAPPING.get(RPSMapping.rock),
        REVERSE_RESPONSE_MOVES_MAPPING.get(RPSMapping.rock)
    ]

    assert get_shapes_based_on_wanted_outcome(
        oponent_moves, wanted_outcomes) == expected_shapes
