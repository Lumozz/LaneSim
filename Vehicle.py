class Vehicle():
    def __init__(self):
        self.x = 0 #meter
        self.y = 0
        self.velocity_x = 0
        self.velocity_y = 0
        self.acceleration_x = 0
        self.acceleration_y = 0

        self.time_step = 0.1 #0.1s

        self.road = None
    def step(self, acceleration_x, acceleration_y):
        self.velocity_x = self.velocity_x + acceleration_x * self.time_step
        self.velocity_y = self.velocity_y + acceleration_y * self.time_step

        self.x = self.x + self.velocity_x * self.time_step
        self.y = self.y + self.velocity_y * self.time_step

