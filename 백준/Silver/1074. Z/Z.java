import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

class Main {
    public static int sol(int n, int r, int c){
        if (n==0)
            return 0;
        return 2*(r%2)+(c%2) + 4*sol(n-1, r/2, c/2);
    }
    public static void main(String[] args) throws IOException {
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int r = sc.nextInt();
        int c = sc.nextInt();
//        int n = Integer.parseInt(br.readLine());
//        int r = Integer.parseInt(br.readLine());
//        int c = Integer.parseInt(br.readLine());

        System.out.println(sol(n,r,c));
    }
}