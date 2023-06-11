class RPSMapping:
    rock = "rock"
    paper = "paper"
    scissors = "scissors"


class OutcomeMapping:
    lose = "X"
    draw = "Y"
    win = "Z"


OPONENT_MOVES_MAPPING = {
    "A": RPSMapping.rock,
    "B": RPSMapping.paper,
    "C": RPSMapping.scissors
}

RESPONSE_MOVES_MAPPING = {
    "X": RPSMapping.rock,
    "Y": RPSMapping.paper,
    "Z": RPSMapping.scissors
}

REVERSE_RESPONSE_MOVES_MAPPING = {
    RPSMapping.rock: "X",
    RPSMapping.paper: "Y",
    RPSMapping.scissors: "Z"
}

OUTCOME_MAPPING = {
    "X": OutcomeMapping.lose,
    "Y": OutcomeMapping.draw,
    "Z": OutcomeMapping.win
}
