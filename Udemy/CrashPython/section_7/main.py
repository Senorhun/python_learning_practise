class Car:
    def __init__(self, name):
        self.max_speed = 80
        self._speed = 0
        self.name = name

    def _get_speed(self):
        return self.speed
    
    def _set_speed(self, speed):
        if speed <= self.max_speed:
            self._speed = speed
        else:
            self._speed = self.max_speed
    
    def accelerate(self, amount):
        self.speed = self.speed + amount
        self.show_speed()
    
    speed = property(
        fget=_get_speed,
        fset=_set_speed
    )
    def brake(self, speed_reduction):
        if self.speed < speed_reduction:
            self.speed = 0
        else:
            self.speed = self.speed - speed_reduction
        self.show_speed()
 
    def show_speed(self):
        print(f"{self.name} is going {self.speed * 10} miles per hour.")
 
 
def draw_road(position):
    global builder
    builder = ROAD[0:position] + CAR_SYMBOL + ROAD[position:len(ROAD)]
    print(builder)
    # builder = builder + road_line + '\n'

def still_on_track(position, road):
   return (position < len(ROAD)) and road[position] == ' '

def drive(speed, direction):
    global car_position
    i = 0
    while i < speed:
        if direction == LEFT:
            car_position = car_position - 1
        elif direction == RIGHT:
            car_position = car_position + 1
        elif direction == STRAIGHT:
            car_position = car_position
        if still_on_track(car_position,ROAD):
            draw_road(car_position)
        else:
            print("OOps game over!")
            return False                    
        i = i + 1
    return True

if __name__ == '__main__':
    ROAD = "|                             |"
    CAR_SYMBOL = "V"
    LEFT = 'a'
    STRAIGHT = 's'
    RIGHT = 'd'
    ACCELERATE = 'w'
    BRAKE = 'x'
    INFO = 'i'
    QUIT_NOW = 'q'
 
    control = ''
    playing = True
    acceleration_factor = 1
    car_position = 15
 
    builder = ''
 
    bat_mobile = Car("The Batmobile")
 
    print("Welcome to the Console Grand Prix")
    print("=================================")
    print()
    print(f"Control your car by pressing '{LEFT}' to go left, and '{RIGHT}' to go right.")
    print(f"'{STRAIGHT}' will go straight.")
    print()
    print("The faster your car's going, the further down the track it")
    print("will travel in the chosen direction.  Watch out for the bends!")
    print()
    print("Choose the acceleration/deceleration factor by pressing a number key.")
    print(f"You can press a number key anytime before using '{ACCELERATE}' or '{BRAKE}'.")
    print(f"Pressing '{ACCELERATE}' will accelerate by that amount,")
    print(f"'{BRAKE}' will brake by that amount.")
    print()
    print("Your car starts off stationary, so you'll need to accelerate before you can move.")
    print()
    print(f"Press '{INFO}' to find out your current speed.")
    print()
    print(f"'{QUIT_NOW}' will quit.")
 
    while playing:
        control = input().lower()
        if control.isnumeric():
            acceleration_factor = int(control)
        else:
            if control == LEFT:
                playing = drive(bat_mobile.speed, control)
            elif control == STRAIGHT:
                playing = drive(bat_mobile.speed, control)
            elif control == RIGHT:
                playing = drive(bat_mobile.speed, control)
            elif control == ACCELERATE:
                bat_mobile.accelerate(acceleration_factor)
            elif control == BRAKE:
                bat_mobile.brake(acceleration_factor)
            elif control == INFO:
                bat_mobile.show_speed()
            elif control == QUIT_NOW:
                # sys.exit()
                playing = False