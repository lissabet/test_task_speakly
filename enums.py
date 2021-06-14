from enum import Enum


class ActionName(Enum):
    INCORRECT_ANSWER = "incorrect_answer"
    CORRECT_ANSWER = "correct_answer"
    WORD_LEARNT = "word_learnt"
