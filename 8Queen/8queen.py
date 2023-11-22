numQueens = 8

cur_sol = [1, 2, 4, 5, 7, 0, 6, 3]
solns = []


def isSafe(testRow, testCol):
    if testRow == 0:
        return True

    for row in range(0, testRow):

        if testCol == cur_sol[row]:
            return False

        if abs(testRow - row) == abs(testCol - cur_sol[row]):
            return False

    return True


for queen0 in range(numQueens):
    if not isSafe(0, queen0):
        continue
    else:
        cur_sol[0] = queen0

    for queen1 in range(numQueens):
        if not isSafe(1, queen1):
            continue
        else:
            cur_sol[1] = queen1

        for queen2 in range(numQueens):
            if not isSafe(2, queen2):
                continue
            else:
                cur_sol[2] = queen2

            for queen3 in range(numQueens):
                if not isSafe(3, queen3):
                    continue
                else:
                    cur_sol[3] = queen3

                for queen4 in range(numQueens):
                    if not isSafe(4, queen4):
                        continue
                    else:
                        cur_sol[4] = queen4

                    for queen5 in range(numQueens):
                        if not isSafe(5, queen5):
                            continue
                        else:
                            cur_sol[5] = queen5

                        for queen6 in range(numQueens):
                            if not isSafe(6, queen6):
                                continue
                            else:
                                cur_sol[6] = queen6

                            for queen7 in range(numQueens):
                                if not isSafe(7, queen7):
                                    continue
                                else:
                                    cur_sol[7] = queen7
                                    solns.append(cur_sol.copy())
                        state = cur_sol

                        horizontal_collisions = sum([state.count(col) - 1 for col in state]) / 2

                        diagonal_collisions = 0
                        for i, col in enumerate(state):
                            for j, diagonal in enumerate(state):
                                mod = abs(i - j)
                                if mod < 0:
                                    if diagonal + mod == col or diagonal - mod == col:
                                        diagonal_collisions += 1
                        diagonal_collisions /= 2
                        fitness = int(28 - (horizontal_collisions + diagonal_collisions))

for soln in solns:
    print('iteration', i)
    print('Current Best', *soln, sep=' ')
    print('fitness =', fitness)
