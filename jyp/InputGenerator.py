import random

f = open('eval_input.txt', 'w')

# T : 테스트 케이스 개수
# sample_input.txt : T = 5
# eval_input.txt : T = 50
T = 50
f.write(str(T) + '\n')
for tc in range(1, T+1):
    # N : N * N 행렬
    # sample_input.txt : range(4, 11)
    # eval_input.txt : range(4, 51)
    N = random.choice(range(4, 51))
    f.write(str(N) + '\n')
    arr = [[0]*N for _ in range(N)]
    idx_list = []
    for i in range(N):
        for j in range(N):
            if (i == 0 and j == 0) or (i == N-1 and j == N-1):
                continue
            else:
                idx_list.append((i, j))
                arr[i][j] = random.choice(range(10))

    # how_many_pick : -1 아이템 개수 0 ~ 5개
    how_many_pick = random.choice(range(6))
    selected_idx_list = random.sample(idx_list, how_many_pick)
    for i, j in selected_idx_list:
        arr[i][j] = -1

    for row in arr:
        str_row = ''
        for idx, num in enumerate(row):
            if idx == N - 1:
                str_row += str(num)
            else:
                str_row += str(num) + ' '
        f.write(str_row + '\n')
f.close()