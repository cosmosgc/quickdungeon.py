import tkinter as tk
import random

# Dungeon size
DUNGEON_WIDTH = 200
DUNGEON_HEIGHT = 200

# Room size
MIN_ROOM_WIDTH = 3
MAX_ROOM_WIDTH = 20
MIN_ROOM_HEIGHT = 3
MAX_ROOM_HEIGHT = 20

class DungeonGenerator:
    def __init__(self, dungeon_width, dungeon_height):
        self.dungeon_width = dungeon_width
        self.dungeon_height = dungeon_height
        self.dungeon = [[0] * self.dungeon_width for _ in range(self.dungeon_height)]

    def generate_dungeon(self):
        self._create_rooms()
        self._create_corridors()
        return self.dungeon

    def _create_rooms(self):
        for _ in range(10):  # Adjust the number of rooms as desired
            room_width = random.randint(MIN_ROOM_WIDTH, MAX_ROOM_WIDTH)
            room_height = random.randint(MIN_ROOM_HEIGHT, MAX_ROOM_HEIGHT)
            x = random.randint(1, self.dungeon_width - room_width - 1)
            y = random.randint(1, self.dungeon_height - room_height - 1)
            self._create_room(x, y, room_width, room_height)

    def _create_room(self, x, y, width, height):
        for i in range(y, y + height):
            for j in range(x, x + width):
                self.dungeon[i][j] = 1

    def _create_corridors(self):
        for row in range(self.dungeon_height):
            for col in range(self.dungeon_width):
                if self.dungeon[row][col] == 1:
                    self._create_corridor(row, col)

    def _create_corridor(self, row, col):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(directions)

        for direction in directions:
            dx, dy = direction
            next_row = row + dy
            next_col = col + dx

            if self._is_valid_position(next_row, next_col) and self.dungeon[next_row][next_col] == 0:
                self.dungeon[next_row][next_col] = 2  # 2 represents a corridor
                self._create_corridor(next_row, next_col)
                return

    def _is_valid_position(self, row, col):
        return 0 <= row < self.dungeon_height and 0 <= col < self.dungeon_width

def draw_dungeon(canvas, dungeon):
    canvas.delete("all")
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()

    cell_width = canvas_width // len(dungeon[0])
    cell_height = canvas_height // len(dungeon)

    for row in range(len(dungeon)):
        for col in range(len(dungeon[0])):
            x1 = col * cell_width
            y1 = row * cell_height
            x2 = x1 + cell_width
            y2 = y1 + cell_height

            if dungeon[row][col] == 1:  # Room
                canvas.create_rectangle(x1, y1, x2, y2, fill="white")
            elif dungeon[row][col] == 2:  # Corridor
                canvas.create_rectangle(x1, y1, x2, y2, fill="gray")

def generate_dungeon():
    dungeon = DungeonGenerator(DUNGEON_WIDTH, DUNGEON_HEIGHT)
    dungeon_data = dungeon.generate_dungeon()
    draw_dungeon(canvas, dungeon_data)

# Create the main window
window = tk.Tk()
window.title("Random Dungeon Generator")

# Create the canvas
canvas = tk.Canvas(window, width=400, height=400)
canvas.pack()

# Create the button
button = tk.Button(window, text="Generate Dungeon", command=generate_dungeon)
button.pack()

# Start the main loop
window.mainloop()
