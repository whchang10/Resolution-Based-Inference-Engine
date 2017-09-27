def apply_neg_to_literal(literal):
    if isinstance(literal, list) and literal[0] == "not":
        assert(len(literal) == 2)
        neg_literal = literal[1]
    else:
        neg_literal = ["not", literal]

    return neg_literal


def apply_neg_to_operator(operator):
    if operator == "and":
        return "or"
    elif operator == "or":
        return "and"
    assert False


def is_empty(sentence):
    if isinstance(sentence, list) and len(sentence) == 0:
        return True
    return False


def is_operator(symbol):
    if isinstance(symbol, basestring) and\
            (symbol == "or" or symbol == "and" or symbol == "implies" or symbol == "biconditional"):
        return True
    return False


def is_literal(symbol):
    if isinstance(symbol, list):
        if symbol[0] == "not":
            assert (len(symbol) == 2)
            return True
    elif isinstance(symbol, basestring):
        if not is_operator(symbol):
            return True
    return False


def is_sentence(obj):
    if not is_literal(obj):
        return True
    return False


def to_string(obj):
    if not isinstance(obj, basestring):
        obj = str(obj)
    return obj


def literal_to_list(obj):
    if (not isinstance(obj, list)) or (isinstance(obj, list) and obj[0] == "not"):
        obj = [obj]
    return obj


def remove_or(clause):
    if clause[0] == "or":
        return clause[1:]
    return clause


def add_to_sentence_set(sentence_set, sentence):
    if is_sentence(sentence) and sentence[0] == "and":
        for clause in sentence[1:]:
            sentence_set.append(clause)
    else:
        sentence_set.append(sentence)


def apply_neg_to_sentence(sentence):
    if is_literal(sentence):
        return apply_neg_to_literal(sentence)
    neg_sentence = []
    for symbol in sentence:
        if is_operator(symbol):
            neg_sentence.append(apply_neg_to_operator(symbol))
        elif is_literal(symbol):
            neg_sentence.append(apply_neg_to_literal(symbol))
        else:
            assert False

    return neg_sentence
