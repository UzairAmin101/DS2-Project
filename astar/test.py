from astar.skew_heap import skewHeap


def shortest_path(grid, start, target):
    sd = {}
    parent = {}
    visited = []
    pq = skewHeap()
    pq.enqueue(0, start)

    for row in grid:
        for node in row:
            if node == start:
                sd[node] = 0
            sd[node] = 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000

    while not pq.is_empty():
        x = pq.dequeue()

        if x == target:
            backtrack(parent, target, win, grid, ROWS, width)
            target.set_target()
            return True

        for neighbour in x.neighbours:

            new_dist = sd[x] + 1

            if new_dist < sd[neighbour]:
                sd[neighbour] = new_dist
                parent[neighbour] = x

            if neighbour not in pq.dfs() and neighbour not in visited:
                pq.enqueue(neighbour)
                visited.append(neighbour)
                neighbour.set_open()

        draw(win, grid, ROWS, width)

        # Since we have updated the values for all the neighbours of this node, we will set its state to explored
        if node != start:
            node.set_explored()

    return False
