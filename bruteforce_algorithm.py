# Brute force method
# The value of C(n, k) can be recursively calculated using the following standard formula for Binomial Coefficients.
# C(n, k) = C(n-1, k-1) + C(n-1, k)
# C(n, 0) = C(n, n) = 1
def binomialCoeff_BF(n, k):
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1

    # Recursive Call
    return binomialCoeff_BF(n - 1, k - 1) + binomialCoeff_BF(n - 1, k)


# Divide and Conquer method
# re-computations of the same subproblems can be avoided by constructing a temporary 2D-array C[][] in a bottom-up manner.
# uses Overlapping Subproblems concep


def binomialCoef_DC(n, k):
    C = [[0 for x in range(k + 1)] for x in range(n + 1)]

    # Calculate value of Binomial
    # Coefficient in bottom up manner
    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            # Base Cases
            if j == 0 or j == i:
                C[i][j] = 1

            # Calculate value using
            # previously stored values
            else:
                C[i][j] = C[i - 1][j - 1] + C[i - 1][j]
    return C[n][k]


# Main block
n = int(input("Enter n :"))
k = int(input("Enter k :"))
print("Brute Force method n^k : ", binomialCoeff_BF(n, k))
print("Divide and Conquer n^k : ", binomialCoef_DC(n, k))