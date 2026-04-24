def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    means = []
    if mode == "column":
        n = len(matrix[0]) # get length of the first nested list
        col_index = 0

        while(n != 0):
            col_mean = 0
            col_height = 0

            for row in matrix:
                col_mean += row[col_index]
                col_height += 1

            n -= 1
            col_index += 1
            means.append(col_mean / col_height)

    elif mode == "row":
        for row in matrix:
            row_mean = 0
            for n in row:
                row_mean += n

            means.append(row_mean / len(row))

    return means

print(calculate_matrix_mean([[1, 2, 3, 4], [5, 6, 7, 8]], 'column'))
