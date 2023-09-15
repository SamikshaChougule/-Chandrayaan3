class LunarCraft:
    def _init_(self, x, y, z, direction):
        self.x = x
        self.y = y
        self.z = z
        self.direction = direction

    def move_forward(self):
        if self.direction == 'N':
            self.y += 1
        elif self.direction == 'S':
            self.y -= 1
        elif self.direction == 'E':
            self.x += 1
        elif self.direction == 'W':
            self.x -= 1
        elif self.direction == 'Up':
            self.z += 1
        elif self.direction == 'Down':
            self.z -= 1

    def move_backward(self):
        if self.direction == 'N':
            self.y -= 1
        elif self.direction == 'S':
            self.y += 1
        elif self.direction == 'E':
            self.x -= 1
        elif self.direction == 'W':
            self.x += 1
        elif self.direction == 'Up':
            self.z -= 1
        elif self.direction == 'Down':
            self.z += 1

    def turn_left(self):
        if self.direction == 'N':
            self.direction = 'W'
        elif self.direction == 'S':
            self.direction = 'E'
        elif self.direction == 'E':
            self.direction = 'N'
        elif self.direction == 'W':
            self.direction = 'S'

    def turn_right(self):
        if self.direction == 'N':
            self.direction = 'E'
        elif self.direction == 'S':
            self.direction = 'W'
        elif self.direction == 'E':
            self.direction = 'S'
        elif self.direction == 'W':
            self.direction = 'N'

    def turn_up(self):
        if self.direction in ('N', 'S'):
            self.direction = 'Up'

    def turn_down(self):
        if self.direction == 'Up':
            self.direction = 'Down'

    def execute_commands(self, commands):
        for command in commands:
            if command == 'f':
                self.move_forward()
            elif command == 'b':
                self.move_backward()
            elif command == 'l':
                self.turn_left()
            elif command == 'r':
                self.turn_right()
            elif command == 'u':
                self.turn_up()
            elif command == 'd':
                self.turn_down()

    def get_position(self):
        return (self.x, self.y, self.z)

    def get_direction(self):
        return self.direction

# User input for initial position and commands
x = int(input("Enter initial X position: "))
y = int(input("Enter initial Y position: "))
z = int(input("Enter initial Z position: "))
direction = input("Enter initial direction (N, S, E, W, Up, Down): ")
commands = input("Enter commands (e.g., 'frubl'): ")

# Create the LunarCraft object with user-provided input
craft = LunarCraft(x, y, z, direction)

# Execute the user-provided commands
craft.execute_commands(commands)

# Get and print the final position and direction
final_position = craft.get_position()
final_direction = craft.get_direction()
print("Final Position:", final_position)
print("Final Direction:", final_direction
