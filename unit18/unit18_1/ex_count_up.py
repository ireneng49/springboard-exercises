def count_up(start, stop):
    """Print all numbers from start up to and including stop.

    For example:

        count_up(5, 7)

   should print:

        5
        6
        7
    """

    # YOUR CODE HERE
    input = range(start,stop+1)
    for x in input:
        print(x)

count_up(5, 10)        

"""
solution:
def count_up(start, stop):
    while start <= stop:
        print(start)
        start = start + 1
"""