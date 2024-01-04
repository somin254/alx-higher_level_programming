#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    yote = dir()
    for i in range(0, len(yote)):
        if yote[i][:2] != "__":
            print("{:s}".format(yote[i]))
