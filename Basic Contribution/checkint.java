import java.util.Scanner;

class checkint{
    static boolean isNumber(String s)
    {
        for (int i = 0; i < s.length(); i++)
            if (Character.isDigit(s.charAt(i)) == false)
                return false;

        return true;
    }

    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
	System.out.print("Enter : ");
        String num = in.nextLine();
        System.out.print("Is it Integer : " + isNumber(num));
    }
}