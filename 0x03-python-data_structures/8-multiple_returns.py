#1/usr/bin/python3
def multiple_returns(sentence):
    tuple_return = ()
    if len(sentence) == 0:
        tuple_return = 0, "None"
    else:
        tuple_return = len(sentence), sentence[0]
    return tuple_return
