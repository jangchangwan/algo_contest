import sys
sys.stdin = open('input.txt', 'r')
# sys.stdin = open('eval_input.txt', 'r')

def DFS(r, c, total, power, visited):
    global min_ans
    # 종료 조건
    if r == (N-1) and c == (N-1):
        min_ans = min(min_ans, total)
        return
    # 가지치기
    if total >= min_ans:
        return

    else:
        # 탐색
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            # 범위 체크
            if (0 <= nr < N) and (0 <= nc < N) and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                # 아이템 획득시
                if arr[nr][nc] == -1:
                    DFS(nr, nc, total, power+1, visited)
                # 아이템 미획득 시
                else:
                    # 나누어 떨어지지 않는 경우
                    cnt = arr[nr][nc] // power
                    if arr[nr][nc] % power:
                        DFS(nr, nc, total + cnt + 1, power, visited)
                    # 나우어 떨어지는 경우
                    else:
                        DFS(nr, nc, total + cnt, power, visited)
                visited[nr][nc] = 0


dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    # 최대로 나올 수 있는 값
    min_ans = N * N * 9
    visited[0][0] = 1
    DFS(0, 0, 0, 1, visited)
    print('#{} {}'.format(tc, min_ans))