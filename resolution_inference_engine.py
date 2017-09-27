import copy

from two_statement_resolution import resolve_imp
from util import add_to_sentence_set, apply_neg_to_sentence, is_empty, is_literal

knowledge_base = []


def tell_imp(sentence):
    add_to_sentence_set(knowledge_base, sentence)


def ask_imp(sentence):
    if sentence == "":
        return True
    resolved_set = copy.deepcopy(knowledge_base)
    add_to_sentence_set(resolved_set, apply_neg_to_sentence(sentence))
    while True:
        new_resolved = []
        for index, left_clause in enumerate(resolved_set):
            for right_clause in resolved_set[index + 1:]:
                resolved_result = resolve_imp(left_clause, right_clause)
                if resolved_result is not False:
                    if is_empty(resolved_result):
                        return True
                    elif is_literal(resolved_result) or\
                        (isinstance(resolved_result, list) and not is_empty(resolved_result)):
                        new_resolved.append(resolved_result)

        resolved_set_len = len(resolved_set)
        for new_sentence in new_resolved:
            if new_sentence not in resolved_set:
                resolved_set.append(new_sentence)
        if resolved_set_len == len(resolved_set):
            return False


def clear_imp():
    global knowledge_base
    knowledge_base = []

