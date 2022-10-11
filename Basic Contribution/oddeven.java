import java.util.Scanner;

class oddeven{

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.print("Enter : ");
        int num = in.nextInt();
        if(num % 2 == 0)
            System.out.print("Even");
        else
            System.out.print("Odd");
    }
}
