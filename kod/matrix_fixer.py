import numpy as np

def try_fix_matrix(M):
    M = M.copy()
    current_arrange = []
    col_reapeats = np.zeros(len(M))

    for i in range(len(M)):
        dominant_col = -1
        for j in range(len(M)):
            dominant_test = np.abs(M[i][j])
            sum = np.sum(np.abs(M[i])) - dominant_test
            if (dominant_test >= sum):
                dominant_col = j
                break
        if dominant_col == -1:
            return False, "no dominant element in row " + str(i)
        current_arrange.append([i, dominant_col])
        col_reapeats[j] += 1
        if col_reapeats[j] > 1:
            return False, "multiple dominant elements in the same col"

    return True, fix_matrix(current_arrange, M)


def fix_matrix(current_arrange, M):

    # sortowanie bąbelkowe xD
    for i in range(len(M) - 1):
        for j in range(len(M) - i - 1):
            if current_arrange[j][1] > current_arrange[j+1][1]:
                current_arrange[j][1], current_arrange[j+1][1] = current_arrange[j+1][1],current_arrange[j][1]
                M[[j, j+1]] = M[[j+1, j]]
    return M