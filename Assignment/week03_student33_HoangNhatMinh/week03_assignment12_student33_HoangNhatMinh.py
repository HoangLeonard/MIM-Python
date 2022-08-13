import itertools
import math

n = 24
dim = math.ceil(math.sqrt(n))

matrix = []
for i in range(dim):
    matrix.append([-1 for j in range(dim)])

point = [0, 0]
if dim % 2 != 0:
    point[0] = dim
else:
    point[0] = -1
    point[1] = dim - 1

move = {
    'up': (-1, 0),
    'right': (0, 1),
    'down': (1, 0),
    'left': (0, -1)
}                           # direction: directional vector


def canMoveTo(d: str, p: list):    # 'd' stands for direction, 'p' stands for checked point
    v = move[d]             # 'v' stands for directional vector
    if p[0] + v[0] < 0 or p[1] + v[1] < 0:
        return False
    try:
        matrix[p[0] + v[0]][p[1] + v[1]]
    except IndexError:
        return False
    else:
        return True


count = dim ** 2
directions = itertools.cycle(move.keys())   # move.keys() = ['up', 'right', 'down', 'left']
direction = directions.__next__()

while count > 0:
    vector = move[direction]
    if canMoveTo(direction, point) and matrix[point[0] + vector[0]][point[1] + vector[1]] == -1:
        point[0] += vector[0]
        point[1] += vector[1]
        matrix[point[0]][point[1]] = count if count <= n else ''
        count -= 1
    else:
        direction = directions.__next__()
        continue

for i in range(dim):
    for j in range(dim):
        print(f'{matrix[i][j]:3}', end='')
    print()