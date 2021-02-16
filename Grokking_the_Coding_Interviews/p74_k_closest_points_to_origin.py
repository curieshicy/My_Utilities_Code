import heapq
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_point(self):
        print("[" + str(self.x) + ", " + str(self.y) + "] ", end='')

def find_closest_points(points, k):
    max_heap = []
    for i in range(k):
        x, y = points[i].x, points[i].y
        heapq.heappush(max_heap, (-(x**2 + y**2), points[i]))
    
    for i in range(k, len(points)):
        new_squared = points[i].x**2 + points[i].y**2
        if new_squared < -max_heap[0][0]:
            heapq.heappushpop(max_heap, (-new_squared, points[i]))
    
    result = []
    for _, point in max_heap:
        result.append(point)
    
    return result


def main():
    result = find_closest_points([Point(1, 3), Point(3, 4), Point(2, -1)], 2)
    print("Here are the k points closest the origin: ", end='')
    for point in result:
        point.print_point()
main()
