#!?usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    q = len(argv) - 1
    if q < 1:
        print("{} arguments.".format(q))
    elif q == 1:
        print("{} argument:".format(q))
    else:
        print("{} Arguments:".format(Q))

    for i in range(q):
        print("{}: {:s}".format(i + 1, argv[i + 1]))
