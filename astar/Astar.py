from operator import ne
import pygame
from node_class import *
from skew_heap import *


# Setting up some window parameters
width = 600
window = pygame.display.set_mode((width, width))
pygame.display.set_caption("DSA Project")


# Using manhattan distance to get the H value for the target node
def h_function(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


# Making a backtracking function which constructs the final path
def backtrack(parent_list, node, win, grid, ROWS, width):
    while node in parent_list:
        node = parent_list[node]
        node.set_path()
        draw(win, grid, ROWS, width)


# Initializing all the nodes in the grid
def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, gap, rows)
            grid[i].append(node)

    return grid


# Function to draw the GUI
def draw(win, grid, rows, width):

    # Displaying a white window
    win.fill(white)
    for row in grid:
        for node in row:
            node.draw(win)

    gap = width // rows

    # Drawing the grid lines on the window
    for i in range(rows):
        pygame.draw.line(win, black, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, black, (j * gap, 0), (j * gap, width))
    pygame.display.update()


# A Start Algorithm for more information: https://www.geeksforgeeks.org/a-search-algorithm/

def algorithm(win, grid, ROWS, width, start, target):

    # queue = []  # Making a priority queue
    queue = skewHeap()
    parent = {}

    f_values = {}
    g_values = {}

    # Making the f and g values
    for row in grid:
        for node in row:
            f_values[node] = 1000000000000000000000000000000000000000000000000000
            g_values[node] = 1000000000000000000000000000000000000000000000000000

    # queue = enqueue(queue, (0, start))
    queue.enqueue(0, start)
    f_values[start] = h_function(start.position(), target.position())
    g_values[start] = 0

    # Running the loop while the queue is not empty
    while not queue.is_empty():

        # Making sure the code stops if the window is exited
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # node = dequeue(queue)[1]
        node = queue.dequeue()

        # if the node popped from the queue is the target node then call the backtrack function
        if node == target:
            backtrack(parent, target, win, grid, ROWS, width)
            target.set_target()
            return True

        # Updating all the neighbouring nodes
        for neighbour in node.neighbors:

            temp = g_values[node] + 1  # Calculating the new g value

            # If the new g value for the neighbouring nodes is lesser then updating the g and f values of that node
            if temp < g_values[neighbour]:
                parent[neighbour] = node
                g_values[neighbour] = temp
                h_value = h_function(neighbour.position(), target.position())
                f_values[neighbour] = temp + h_value

                # Adding the neighbours of the current node in the queue so they are considered next
                queue_elements = queue.dfs()
                if neighbour not in queue_elements:
                    queue.enqueue(f_values[neighbour], neighbour)
                    neighbour.set_open()

        # Drawing the progress made in each iteration
        draw(win, grid, ROWS, width)

        # Since we have updated the values for all the neighbours of this node, we will set its state to explored
        if node != start:
            node.set_explored()

    return False


# Main function
def main(win, width):

    # setting up parameters
    rows = 50
    grid = make_grid(rows, width)

    start = None
    target = None
    run = True

    # Watching out for events and calling functions based on it
    while run:
        draw(win, grid, rows, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # Checking when left mouse button is pressed
            if pygame.mouse.get_pressed()[0]:

                # Determining which node is pressed
                pos = pygame.mouse.get_pos()

                # Getting the position of the node which the user clicked
                gap = width // rows
                y, x = pos
                row = y // gap
                col = x // gap

                node = grid[row][col]

                # Checks to determine what state to set the node to
                if not start and node != target:
                    start = node
                    start.set_start()

                elif not target and node != start:
                    target = node
                    target.set_target()

                elif node != target and node != start:
                    node.set_wall()

            # Checking when a key on the keyboard is pressed
            if event.type == pygame.KEYDOWN:

                # If the "enter" key is pressed, start the algorithm
                if event.key == pygame.K_RETURN and (start != None and target != None):
                    for row in grid:
                        for node in row:
                            node.refresh_neighbours(grid)

                    algorithm(win, grid, rows, width, start, target)

                # If "r" key is pressed, then reset the grid
                if event.key == pygame.K_r:
                    start = None
                    target = None
                    grid = make_grid(rows, width)

    pygame.quit()


main(window, width)
