import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Scanner;
import java.util.StringTokenizer;

class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[] arrInput = new int[n];
        int[] arrSum = new int[n];
        int tmp;

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            tmp = Integer.parseInt(st.nextToken());
            arrInput[i] = tmp;
            if (i == 0) arrSum[i] = tmp;
            else arrSum[i] += (arrSum[i-1] + tmp);
        }

        for (int i = 0; i < m; i++){
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken()) - 1;
            int end = Integer.parseInt(st.nextToken()) - 1;
//            System.out.println(end +" " + start);
            if (start == 0) System.out.println(arrSum[end]);
            else System.out.println(arrSum[end] - arrSum[start-1]);
        }
    }
}