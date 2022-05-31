# jyp 풀이
# 2022-05-31

import sys
# sys.stdin = open('sample_input.txt', 'r')
sys.stdin = open('eval_input.txt')


def game(i, j, power, ans):
    global arr, N, min_ans, visited
    if 0 <= i < N and 0 <= j < N:
        if ans >= min_ans:
            return
        if i == N-1 and j == N-1:
            if ans < min_ans:
                min_ans = ans
            return
        visited[i][j] = 1
        if arr[i][j] == -1:
            power += 1
        else:
            if arr[i][j]/power > int(arr[i][j]/power):
                ans += arr[i][j]//power + 1
            else:
                ans += arr[i][j]//power
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if 0 <= i + di < N and 0 <= j + dj < N:
                if visited[i+di][j+dj] == 0:
                    game(i + di, j + dj, power, ans)
                    visited[i+di][j+dj] = 0
    else:
        return


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    min_ans = 9 * (N ** 2)
    game(0, 0, 1, 0)
    print('#'+str(tc), min_ans)