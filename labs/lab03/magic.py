def magic(n):
    m = []
    for i in range(n):
        m.append([0] * n)
    row, col = n - 1, n // 2
    for k in range(0, n * n):
        m[row][col], newRow, newCol = (k + 1), (row + 1) % n, (col + 1) % n
        if m[newRow][newCol] == 0:
            row, col = newRow, newCol
        else:
            row, col = row - 1, col
    return m


def show(m):
    for i in range(len(m)):
        for j in range(len(m)):
            print(("   " + str(m[i][j]))[-3:], end=" ")
        print()


import numpy as np


def np_is_magic(square):
    np_square = np.array(square)

    # Row sum
    row_sum = np.sum(np_square, axis=0)

    # Column sum
    col_sum = np.sum(np_square, axis=1)

    # Diagonal 1 sum
    d1_sum = np.trace(np_square)

    # Diagonal 2 sum
    d2_sum = np.trace(np.flip(np_square))

    # Checks if all elements are the same
    rows = all(ele == row_sum[0] for ele in row_sum)
    cols = all(ele == col_sum[0] for ele in col_sum)

    # Checks if diagonal sums are same as row sums
    d1 = d1_sum == row_sum[0]
    d2 = d2_sum == row_sum[0]

    # Checks if row, column, and both diagonal sums are equal
    if rows == cols == d1 == d2:
        print("Magic")
    else:
        print("Not magic")


def main():
    l = magic(5)
    show(l)
    np_is_magic(l)


if __name__ == "__main__":
    main()

