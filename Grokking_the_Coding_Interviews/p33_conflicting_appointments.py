def can_attend_all_appointments(intervals):
    if len(intervals) < 2:
        return True
    intervals.sort(key = lambda t: (t[0], t[1]))
    start, end = intervals[0]
    for i in range(1, len(intervals)):
        new_start, new_end = intervals[i]
        if new_start < end:
            return False
        else:
            start, end = new_start, new_end
            
    return True
        

def main():
  print("Can attend all appointments: " + str(can_attend_all_appointments([[1, 4], [2, 5], [7, 9]])))
  print("Can attend all appointments: " + str(can_attend_all_appointments([[6, 7], [2, 4], [8, 12]])))
  print("Can attend all appointments: " + str(can_attend_all_appointments([[4, 5], [2, 3], [3, 6]])))


main()
