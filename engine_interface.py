from two_statement_resolution import resolve_imp
from resolution_inference_engine import tell_imp, ask_imp, clear_imp


def resolve(left_clause, right_clause):
    return resolve_imp(left_clause, right_clause)


def TELL(sentence):
    return tell_imp(sentence)


def ASK(sentence):
    return ask_imp(sentence)


def CLEAR():
    return clear_imp()

