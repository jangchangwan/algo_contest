import java.io.*;
import java.util.*;

class Solution {
	static final int[] dx = { -1, 1, 0, 0 };
	static final int[] dy = { 0, 0, -1, 1 };
	static int[][] map;
	static boolean[][] visit;
	static int n, ans;
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int tc = Integer.parseInt(br.readLine());
		for (int t = 1; t <= tc; t++) {
			ans = Integer.MAX_VALUE;
			n = Integer.parseInt(br.readLine());
			map = new int[n][n]; // 하수구 도면
			visit = new boolean[n][n];
			for (int i = 0; i < n; i++) {
				StringTokenizer st = new StringTokenizer(br.readLine());
				for (int j = 0; j < n; j++) {
					map[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			visit[0][0] = true;
			dfs(0, 0, 0, 1); // DFS
			sb.append("#").append(t).append(" ").append(ans).append("\n");
		}
		System.out.print(sb.toString());
	}
	static void dfs(int x, int y, int cnt, int power) {
		if (cnt >= ans) { // 가지 치기
			return;
		}
		if (x == n - 1 && y == n - 1) { // 종료 조건
			ans = Math.min(ans, cnt);
			return;
		}
		if (map[x][y] == -1) { // 아이템 획득
			power++;
		} else if (map[x][y] > 0) { // 청소
			cnt += (map[x][y] - 1) / power + 1;
		}
		for (int d = 0; d < 4; d++) { // 사방 탐색
			int nx = x + dx[d];
			int ny = y + dy[d];
			if (nx >= 0 && nx < n && ny >= 0 && ny < n && !visit[nx][ny]) {
				visit[nx][ny] = true;
				dfs(nx, ny, cnt, power);
				visit[nx][ny] = false;
			}
		}
	}
}