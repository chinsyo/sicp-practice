def ackermanns_function(x, y):
    if y == 0:
        return 0
    if x == 0:
        return 2 * y
    if y == 1:
        return 2
    return ackermanns_function(x-1, ackermanns_function(x, y-1))

if __name__ == '__main__':
    ret = ackermanns_function(1, 10)
    print("ackermanns_function(1, 10) = %d" % ret)
    ret = ackermanns_function(2, 4)
    print(ret)
    ret = ackermanns_function(3, 3)
    print(ret)
