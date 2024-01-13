import math


class Line:
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
        def intersects(point, line_p1, line_p2):
            # 检查水平射线是否与线段相交
            (x1, y1), (x2, y2) = line_p1, line_p2
            x, y = point

            # 如果点在线段之外，没有交点
            if y < min(y1, y2) or y > max(y1, y2) or x > max(x1, x2):
                return False

            # 如果线段水平，需要特别处理
            if y1 == y2:
                return y == y1

            # 计算交点的x坐标
            intersect_x = x1 + (x2 - x1) * (y - y1) / (y2 - y1)
            return intersect_x >= x

        count = 0

        if intersects(point, self.left_line.start, self.left_line.end):
            count += 1
        if intersects(point, self.left_line.end, self.right_line.end):
            count += 1
        if intersects(point, self.right_line.end, self.right_line.start):
            count += 1
        if intersects(point, self.right_line.start, self.left_line.start):
            count += 1

        return count % 2 == 1


class Road:
    def __init__(self):
        self.lane = {}

    def append_lane(self, name, lane):
        if self.lane.get(name, None) is None:
            self.lane[name] = lane
        else:
            print(f"You have created a lane named {name}")

    def which_lane(self, vehicle):
        for key in self.lane.keys():
            if self.lane[key].is_point_within([vehicle.x, vehicle.y]):
                return key

        return None


if __name__ == "__main__":

    # 简单测试一下Line
    l1 = Line([0, 0], [100, 0])
    l2 = Line([100, 0], [200, 3.5])

    print(l1)
    print(l2)

    # 简单测试一下Lane
    left_line = Line([0, 0], [10, 10])
    right_line = Line([10, 0], [20, 10])

    lane = Lane(left_line, right_line)
    point = (5, 5)
    print("点是否在车道内:", lane.is_point_within(point))
    print("左边界距离:", lane.distance_to_lines(point)[0])
    print("右边界距离:", lane.distance_to_lines(point)[1])

    # 简单测试一下Road

    l1 = Line([0, 7], [100, 7])
    l2 = Line([0, 3.5], [100, 3.5])
    l3 = Line([0, 0], [100, 0])

    l4 = Line([100, 7], [200, 7])
    l5 = Line([100, 0], [200, 3.5])

    l6 = Line([200, 7], [300, 7])
    l7 = Line([200, 3.5], [300, 3.5])

    lane1 = Lane(l1, l2)
    lane2 = Lane(l2, l3)
    lane3 = Lane(l4, l5)
    lane4 = Lane(l6, l7)

    road = Road()
    road.append_lane('lane1', lane1)
    road.append_lane('lane2', lane2)
    road.append_lane('lane3', lane3)
    road.append_lane('lane4', lane4)

    from Vehicle import Vehicle

    car = Vehicle()
    car.x = 1
    car.y = 1.75

    # 生成一辆车，让他按照1m/s**2的加速度行驶200个时间步（20s）
    for i in range(0, 200):
        car.step(1, 0)
        current_lane = road.which_lane(car)
        print(f"current position x: {car.x}m    "
              f"current position y: {car.y}m    "
              f"current speed x   : {car.velocity_x}    "
              f"current lane      : {current_lane} \n")
