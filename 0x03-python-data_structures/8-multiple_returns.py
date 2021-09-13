#1/usr/bin/python3
def multiple_returns(sentence):
    tuple_return = ()
    length = len(sentence)
    if length == 0:
        tuple_return = 0, "None"
    else:
        tuple_return = (length, sentence[0])
    return tuple_return
