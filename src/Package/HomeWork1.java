package Package;

import java.util.Scanner;

public class HomeWork1 {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int nums [] = new int[3];
		int max = -999999;
		for (int i = 0; i < nums.length; i++) {
			nums[i] = sc.nextInt();
			if (nums[i] > max) {
				max = nums[i];
			}
		}
		System.out.println(max);
		sc.close();
	}

}
