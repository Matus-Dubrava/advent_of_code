import os
import sys

from typing import List, Set

from rock_paper_scissors_mappings import RPSMapping, OutcomeMapping, OPONENT_MOVES_MAPPING, \
    RESPONSE_MOVES_MAPPING, REVERSE_RESPONSE_MOVES_MAPPING, OUTCOME_MAPPING
from helpers.validation import validate_file_input, handle_file_not_found


def load_strategy_guide(file_path: str) -> Set[List[str]]:
    oponent_moves = []
    responses = []

    try:
        with open(file_path, "r") as f:
            for line in f:
                line = line.strip()

                oponent_move, response = line.split(" ")
                oponent_moves.append(oponent_move)
                responses.append(response)

        return (oponent_moves, responses)
    except FileNotFoundError as err:
        handle_file_not_found(file_path)


def get_shape_based_on_wanted_outcome(oponent_move: str, wanted_outcome: str) -> str:
    oponent_move = OPONENT_MOVES_MAPPING.get(oponent_move)
    wanted_outcome = OUTCOME_MAPPING.get(wanted_outcome)

    if oponent_move == RPSMapping.rock:
        if wanted_outcome == OutcomeMapping.win:
            return REVERSE_RESPONSE_MOVES_MAPPING.get(RPSMapping.paper)
        if wanted_outcome == OutcomeMapping.draw:
            return REVERSE_RESPONSE_MOVES_MAPPING.get(RPSMapping.rock)
        if wanted_outcome == OutcomeMapping.lose:
            return REVERSE_RESPONSE_MOVES_MAPPING.get(RPSMapping.scissors)

    if oponent_move == RPSMapping.paper:
        if wanted_outcome == OutcomeMapping.win:
            return REVERSE_RESPONSE_MOVES_MAPPING.get(RPSMapping.scissors)
        if wanted_outcome == OutcomeMapping.draw:
            return REVERSE_RESPONSE_MOVES_MAPPING.get(RPSMapping.paper)
        if wanted_outcome == OutcomeMapping.lose:
            return REVERSE_RESPONSE_MOVES_MAPPING.get(RPSMapping.rock)

    if oponent_move == RPSMapping.scissors:
        if wanted_outcome == OutcomeMapping.win:
            return REVERSE_RESPONSE_MOVES_MAPPING.get(RPSMapping.rock)
        if wanted_outcome == OutcomeMapping.draw:
            return REVERSE_RESPONSE_MOVES_MAPPING.get(RPSMapping.scissors)
        if wanted_outcome == OutcomeMapping.lose:
            return REVERSE_RESPONSE_MOVES_MAPPING.get(RPSMapping.paper)


def get_shapes_based_on_wanted_outcome(oponent_moves: List[str], wanted_outcomes: List[str]) -> str:
    shapes = []

    for oponent_move, wanted_outcome in zip(oponent_moves, wanted_outcomes):
        shapes.append(get_shape_based_on_wanted_outcome(
            oponent_move, wanted_outcome))

    return shapes


def get_outcome_points(oponent_move: str, response: str) -> int:
    """
    Based on the rules of the game, decide whether this leads to loss, draw or win for you.
    Return number of points: loss - 0, draw - 3, win - 6.
    """

    oponent_move = OPONENT_MOVES_MAPPING.get(oponent_move)
    response = RESPONSE_MOVES_MAPPING.get(response)

    if oponent_move == RPSMapping.rock:
        if response == RPSMapping.rock:
            return 3
        if response == RPSMapping.paper:
            return 6
        if response == RPSMapping.scissors:
            return 0

    if oponent_move == RPSMapping.paper:
        if response == RPSMapping.rock:
            return 0
        if response == RPSMapping.paper:
            return 3
        if response == RPSMapping.scissors:
            return 6

    if oponent_move == RPSMapping.scissors:
        if response == RPSMapping.rock:
            return 6
        if response == RPSMapping.paper:
            return 0
        if response == RPSMapping.scissors:
            return 3


def compute_one_round_points(oponent_move: str, response: str) -> int:
    """
    oponent move: A - rock, B - paper, C - scissors
    respone:      X - rock, Y - paper, C - scissors

    points for chosen shape: rock - 1, paper - 2, scissors - 3
    """

    def _get_points_for_shape(shape: str) -> int:
        shape = RESPONSE_MOVES_MAPPING.get(shape)

        if shape == RPSMapping.rock:
            return 1
        if shape == RPSMapping.paper:
            return 2
        if shape == RPSMapping.scissors:
            return 3

    points_for_shape = _get_points_for_shape(response)
    outcome_points = get_outcome_points(oponent_move, response)

    return points_for_shape + outcome_points


def compute_total_points(oponent_moves: List[str], responses: List[str]) -> int:
    total_points = 0

    for oponent_move, response in zip(oponent_moves, responses):
        total_points += compute_one_round_points(oponent_move, response)

    return total_points


if __name__ == "__main__":
    validate_file_input(sys.argv)
    file_path = sys.argv[1]

    # oponent_moves, responses = load_strategy_guide(file_path)
    # print(f"total points: {compute_total_points(oponent_moves, responses)}")

    oponent_moves, wanted_outomes = load_strategy_guide(file_path)
    shapes_to_play = get_shapes_based_on_wanted_outcome(
        oponent_moves, wanted_outomes)

    print(
        f"total points: {compute_total_points(oponent_moves, shapes_to_play)}")
