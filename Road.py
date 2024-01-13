import math


class Line():
    def __init__(self, start: list, end: list, solid: bool = True):
        self.start = start
        self.end = end
        self.solid = solid

    def __str__(self):
        len_x = abs(self.start[0] - self.end[0])
        len_y = abs(self.start[1] - self.end[1])

        s = ("solid _____" if self.solid else "dashed _ _ _") + "\n" + \
            f"start   : {self.start}" + "\n" + \
            f"end     : {self.end}" + "\n" + \
            f"length_x： {abs(self.start[0] - self.end[0])}" + "\n" + \
            f"length_y： {abs(self.start[1] - self.end[1])}" + "\n" + \
            f"length  ： {math.sqrt(len_x * len_x + len_y * len_y)}" + "\n"

        return s

class Lane:
    def __init__(self, left_line, right_line):
        self.left_line = left_line
        self.right_line = right_line

    def point_to_line_distance(self, point, line_start, line_end):
        x0, y0 = point
        x1, y1 = line_start
        x2, y2 = line_end

        num = abs((y2 - y1) * x0 - (x2 - x1) * y0 + x2 * y1 - y2 * x1)
        den = math.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)
        return num / den

    def distance_to_lines(self, point):
        left_distance = self.point_to_line_distance(point, self.left_line.start, self.left_line.end)
        right_distance = self.point_to_line_distance(point, self.right_line.start, self.right_line.end)
        return left_distance, right_distance

    def is_point_within(self, point):
        # 这个方法假设车道是直线，且左右车道线平行
        left_distance, right_distance = self.distance_to_lines(point)
        return left_distance + right_distance > self.point_to_line_distance(self.left_line.start, self.right_line.start, self.right_line.end)


if __name__ == "__main__":
    l1 = Line([0, 0], [100, 0])
    l2 = Line([100, 0], [200, 3.5])

    print(l1)
    print(l2)
