class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        R = r - l + 1
        
        # 2*R states: 0 to R-1 for 'less than', R to 2R-1 for 'greater than'
        T_size = 2 * R
        matrix = [[0] * T_size for _ in range(T_size)]
        
        # Constructing the Transition Matrix
        for prev_val in range(R):
            # State: prev_val (current number), True (next must be larger), False (next must be smaller)
            for cur_val in range(R):
                if cur_val != prev_val:
                    # cur_val is smaller -> next must be larger
                    if cur_val < prev_val:
                        matrix[prev_val][cur_val + R] = 1
                    # cur_val is larger -> next must be smaller
                    if cur_val > prev_val:
                        matrix[prev_val + R][cur_val] = 1
                        
        def multiply(A, B):
            C = [[0] * T_size for _ in range(T_size)]
            for i in range(T_size):
                for k in range(T_size):
                    if A[i][k] == 0: continue
                    for j in range(T_size):
                        C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD
            return C
            
        def power(A, p):
            res = [[int(i == j) for j in range(T_size)] for i in range(T_size)]
            while p > 0:
                if p % 2 == 1:
                    res = multiply(res, A)
                A = multiply(A, A)
                p //= 2
            return res

        # Power to n-1
        final_matrix = power(matrix, n - 1)
        
        # Sum all possible valid states from the result
        ans = 0
        for i in range(T_size):
            for j in range(T_size):
                ans = (ans + final_matrix[i][j]) % MOD
                
        return ans

        
