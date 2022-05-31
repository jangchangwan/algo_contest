from math import ceil


def bfs():
    visited = [[1000000]*N for _ in range(N)]
    visited[0][0] = arr[0][0]
    que = [(0, 0, [(0, 0)])]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    while que:
        i, j, bleach = que.pop(0)

        for idx in range(4):
            ni = i + di[idx]
            nj = j + dj[idx]
            if (0 <= ni < N) and (0 <= nj < N) and arr[ni][nj] == -1:
                if (ni, nj) not in bleach:
                    visited[ni][nj] = visited[i][j]
                    bleach.append((ni, nj))
                    que.append((ni, nj, bleach))
            elif (0 <= ni < N) and (0 <= nj < N) and visited[ni][nj] > visited[i][j] + ceil(arr[ni][nj]/len(bleach)):
                visited[ni][nj] = visited[i][j] + ceil(arr[ni][nj]/len(bleach))
                que.append((ni, nj, bleach))
    return visited[N-1][N-1]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = bfs()
    print('#{} {}'.format(tc, ans))
