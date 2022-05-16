import pygame


# Defining colors
grey = (128, 128, 128)
blue = (0, 0, 255)
maroon = (128, 0, 0)
yellow = (255, 255, 0)
white = (255, 255, 255)
black = (0, 0, 0)
purple = (128, 0, 128)


# Making the node class
class Node:

    # Initializing the node class
    def __init__(self, row, col, width, total_rows):
        self.width = width
        self.total_rows = total_rows
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = white
        self.state = "normal"
        self.neighbors = []

    # Defining class functions

    # Returns the position of the node on the grid
    def position(self):
        return self.row, self.col

    # Returns the current state of the node
    def return_state(self):
        return self.state

    # Sets the node state as the start node
    def set_start(self):
        self.color = blue
        self.state = "start"

    # Sets the node state as an explored node
    def set_explored(self):
        self.color = grey
        self.state = "yellow"

    # Sets the node state as an open node
    def set_open(self):
        self.color = purple
        self.state = "open"

    # Sets the node state as a wall node
    def set_wall(self):
        self.color = black
        self.state = "wall"

    # Sets the node state as the target
    def set_target(self):
        self.color = maroon
        self.state = "target"

    # Sets the node state to path
    def set_path(self):
        self.color = yellow
        self.state = "path"

    # Draws the node on the grid
    def draw(self, win):
        pygame.draw.rect(
            win, self.color, (self.x, self.y, self.width, self.width))

    # Updates the list of neighbours of the node
    def refresh_neighbours(self, grid):
        self.neighbors = []
        # Checking for viable neighbours in the spot below
        if self.row < self.total_rows - 1 and not (grid[self.row + 1][self.col].return_state() == "wall"):
            print(self.return_state())
            self.neighbors.append(grid[self.row + 1][self.col])

        # Checking for viable neighbours in the spot above
        if self.row > 0 and not (grid[self.row - 1][self.col].return_state() == "wall"):  # UP
            self.neighbors.append(grid[self.row - 1][self.col])

        # Checking for viable neighbours in the spot to the right
        if self.col < self.total_rows - 1 and not (grid[self.row][self.col + 1].return_state() == "wall"):
            self.neighbors.append(grid[self.row][self.col + 1])

        # Checking for viable neighbours in the spot to the left
        if self.col > 0 and not (grid[self.row][self.col - 1].return_state() == "wall"):
            self.neighbors.append(grid[self.row][self.col - 1])
