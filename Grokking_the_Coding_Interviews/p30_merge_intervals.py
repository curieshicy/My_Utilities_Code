from __future__ import print_function

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


def merge(intervals):
    if len(intervals) < 2:
        return intervals
    merged = []
    intervals.sort(key = lambda t: (t.start, t.end))
    x, y = intervals[0].start, intervals[0].end
    for i in range(1, len(intervals)):
        new_x, new_y = intervals[i].start, intervals[i].end
        if new_x < y:
            y = max(new_y, y)
        else:
            merged.append(Interval(x, y))
            x = new_x
            y = new_y
    
    merged.append(Interval(x, y))
    return merged

def main():
    print("Merged intervals: ", end='')
    for i in merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end='')
    for i in merge([Interval(6, 7), Interval(2, 4), Interval(5, 9)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end='')
    for i in merge([Interval(1, 4), Interval(2, 6), Interval(3, 5)]):
        i.print_interval()
    print()

main()
