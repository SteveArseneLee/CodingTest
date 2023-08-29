import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] dp = new int[n+1];
        for (int x = 2; x < n+1; x++) {
            dp[x] = dp[x-1] +1;
            if (x%2 == 0) dp[x] = Math.min(dp[x], dp[x/2] + 1);
            if (x%3 == 0) dp[x] = Math.min(dp[x], dp[x/3] + 1);
        }
        System.out.println(dp[n]);
        sc.close();
    }
}