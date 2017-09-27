import copy

from util import apply_neg_to_literal, to_string, literal_to_list, remove_or


def resolve_imp(left_clause, right_clause):
    left_clause = remove_or(literal_to_list(left_clause))
    right_clause = remove_or(literal_to_list(right_clause))
    left_clause_dict = {}
    for index_l, literal_l in enumerate(left_clause):
        literal_l = to_string(literal_l)
        left_clause_dict[literal_l] = index_l

    del_index = []
    resolved_result = copy.deepcopy(left_clause)
    for literal_r in right_clause:
        neg_literal = to_string(apply_neg_to_literal(literal_r))
        literal_str = to_string(literal_r)
        assert(not ((left_clause_dict.get(literal_str, None) is not None) and\
                (left_clause_dict.get(neg_literal, None) is not None)))
        if left_clause_dict.get(literal_str, None) is None:
            if left_clause_dict.get(neg_literal, None) is not None:
                del_index.append(left_clause_dict.get(neg_literal))
                if len(del_index) > 1:
                    break
            else:
                resolved_result.append(literal_r)

    if len(del_index) != 1:
        return False
    del resolved_result[del_index[0]]
    if len(resolved_result) == 1:
        resolved_result = resolved_result[0]
    elif len(resolved_result) > 1:
        #resolved_result.sort(key = str.lower)
        resolved_result.insert(0, "or")

    return resolved_result

