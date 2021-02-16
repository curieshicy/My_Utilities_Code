import bisect
class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def find_next_interval(intervals):
    n = len(intervals)
    result = [0 for i in range(n)]
    start_times = []
    end_times = []
    d = {}
    for idx, interval in enumerate(intervals):
        start_times.append((interval.start))
        d[interval.start] = idx
        end_times.append((interval.end, idx))
        
    start_times.sort()
    end_times.sort()
    
    for end_time, idx in end_times:
        start_idx = bisect.bisect_left(start_times, end_time)
        if start_idx == n:
            result[idx] = -1
            continue
        result[idx] = d[start_times[start_idx]]
    return result


def main():
    result = find_next_interval([Interval(2, 3), Interval(3, 4), Interval(5, 6)])
    print("Next interval indices are: " + str(result))

    result = find_next_interval([Interval(3, 4), Interval(1, 5), Interval(4, 6)])
    print("Next interval indices are: " + str(result))
main()
