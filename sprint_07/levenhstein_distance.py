"""
https://contest.yandex.ru/contest/25597/run-report/70046945/

----------------------------- Idea ----------------------------

We use dynamic programming for calculating Levenhstein distances
for prefixes s1[:i] and s2[:j]. To do so, we will store prefixes
in a matrix DP = [(N + 1) x (M + 1)], where N is the number of symbols in the
first row and  M is the number of symbols in the second row.

During the calculating (i, j) cell in DP, we assume that (i-1, j) and
(i, j-1) are already calculated and contains Levenhstein distances
for s1[i-1] and s2[j-1] correspondingly. Then we will update (i, j) as 
follows:
    DP[i, j] = MIN(
        DP[i - 1, j] + 1,  # Insertion from the 1st string
        DP[i, j - 1] + 1,  # Insertion from the 2nd string
        DP[i, j] + (1 if s[i-1] != s[j-1] # Insertion from both string
    )

First row and the first column in DP will have values 0..M and 0..N
correspondingly. As we would insert symbols only from one of the strings
without accounting the second one.

As a result we return the last value DP[N, M] that corresponds to the
prefixes equal to the strings themselves.

Implementation notes:
    * Instead of storing the whole matrix [N x M], where N is the 
      number of rows and M is the number of columns, we store only
      two rows as the computation of the current row depends only 
      on the previous row. After each iteration current row becomes
      previous row for the next iteration.
    * We set N to be bigger than M -> will need less space for storing
      two rows of size M.

------------------------ Time Complexity ----------------------

Let M, N be the lenghts of the given strings. Then we need to process
the whole matrix N x M.
Total: O(N x M)

------------------------ Space Complexity ----------------------

We need 2 * M cells in an array, where M is the min(|string1|, |string2|),
as we set M to be the length of the smaller string (see implementation
details above)

Total: O(M)

"""

def calc_levenstein(s1: str, s2: str) -> int:
    # Let s1 be bigger than s2
    if len(s1) < len(s2):
        s1, s2 = s2, s1

    rows, cols = len(s1), len(s2)
    dp = [list(range(cols+1)), [0] * (cols + 1)]

    for i in range(1, rows + 1):
        # Cacluating the row indexes that alternate each time
        row = i % 2
        row_prev = 1 - row

        # Inital values corresponding the first index in a row
        dp[row_prev][0] = (i - 1)
        dp[row][0] = i

        # Processing DP[i, 1..M] 
        for j in range(1, cols + 1):
            eq = int(s1[i - 1] != s2[j - 1])
            dp[row][j] = min(
                    dp[row_prev][j] + 1,
                    dp[row][j - 1] + 1,
                    dp[row_prev][j - 1] + eq
            )

    return dp[rows % 2][-1]
    

s1 = input()
s2 = input()
print(calc_levenstein(s1, s2))
