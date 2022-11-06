import java.util.*;

class ConvertArrays{
    public Double doubleArr[] = new Double[3];
    public Integer intArr[] = new Integer[3];
    public int x=0, y=0,z=0;
    public void convert(String[] arr){
        int indexD=0, indexI=0;

        for (String s: arr){
            if (s.contains("."))
                doubleArr[indexD++] = Double.valueOf(s);
            else
                intArr[indexI++] = Integer.valueOf(s);
        }
    }
    public <A> void display(A[] arr){
        for (A element: arr){
            System.out.print(element+ " ");
        System.out.println();
        }
    }

}

public class Programming {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in); 
        String arr[] = new String[6];
        for(int i=0; i<arr.length; i++){
            arr[i] = sc.nextLine();
        }

    
        ConvertArrays conArrays = new ConvertArrays();
    conArrays.convert(arr);
    System.out.println("===After conversion Arrays===");
    conArrays.display(conArrays.doubleArr);
    conArrays.display(conArrays.intArr);
    }
}
