def read_input():
    maze = []
    x = int(input())
    for i in range(x):
        maze.append(input())
    return maze, x


def data_structure_for_queue(maze, length_maze):
    S_and_E = []
    steps = [[0] * length_maze for i in range(length_maze)]
    for r in range(length_maze):
        for c in range(length_maze):
            if maze[r][c] == "#":
                steps[r][c] = -1
            if maze[r][c] == "S":
                S_and_E.append((r, c))
            if maze[r][c] == "E":
                S_and_E.append((r, c))
    
    return steps, S_and_E

def valid(row, column, steps):

    if 0 <= row < len(steps) and 0 <= column < len(steps):
        if steps[row][column] == 0:
            return True
    return False

def queue_implementation(adj, S_and_E, structure_maze):
    queue = [((S_and_E[0]), 0)]
    visited = set()
    plus = {(S_and_E[0]): None}

    while len(queue) > 0:
        (r, c), distance = queue.pop(0)
        if (r, c) == S_and_E[1]:
            print("Reached in:", distance)
            break
        
        for dr, dc in adj:
            rr, cc = r + dr, c + dc

            if not valid(rr, cc, structure_maze):
                continue
            if (rr, cc) in visited:
                continue 

            visited.add((rr, cc))
            queue.append(((rr, cc), distance + 1))
            plus[rr,cc] = (r,c)
    else:
        print("Not reached")
    
    if S_and_E[1] in plus:
        (r,c) = S_and_E[1]
        while (r,c) != S_and_E[0]:
            structure_maze[r][c] = '+'
            (r,c) = plus[(r,c)]
    

def main():
    adj = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    maze, length_maze = read_input()
    structure_maze, S_and_E = data_structure_for_queue(maze, length_maze)
    queue_implementation(adj, S_and_E, structure_maze)
    
    sr, sc = S_and_E[0]
    er, ec = S_and_E[1]
    
    structure_maze[sr][sc] = "S"
    structure_maze[er][ec] = "E"

    for row in structure_maze:
        for i in range(len(row)):
            if row[i] == -1:
                print("#", end="")
            elif row[i] == "S":
                print("S", end="")
            elif row[i] == "E":
                print("E", end="")
            elif row[i] == "+":
                print("+", end="")
            else:
                print(" ", end="")
        print()

main()