#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    strings = dir(hidden_4)
    for i in range(0, len(strings)):
        if strings[i][0:2] != "__":
            print("{}".format(strings[i]))
