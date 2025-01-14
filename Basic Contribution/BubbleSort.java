import java.util.Scanner;
class BubbleSort
{
    void bubbleSort(int a[])
    {
        int n = a.length;
        for (int i = 0; i < n-1; i++)
            for (int j = 0; j < n-i-1; j++)
                if (a[j] > a[j+1])
                {
                    int temp = a[j];
                    a[j] = a[j+1];
                    a[j+1] = temp;
                }
    }
 
    void printArray(int a[])
    {
        int n = a.length;
        for (int i=0; i<n; ++i)
          System.out.print(a[i] + " ");
        System.out.println();
    }
 
    
    public static void main(String args[])
    {
	Scanner scan =new Scanner(System.in);
        BubbleSort ob = new BubbleSort();
	System.out.println("Enter size of array:");
	int size=scan.nextInt();
	int arr[] = new int[size];
	System.out.println("Enter array:");
	for(int i=0;i<size;i++)
		arr[i]=scan.nextInt();
        ob.bubbleSort(arr);
        System.out.println("Sorted array");
        ob.printArray(arr);
    }
}