import java.util.*;
class ArrayExample <T>{
  T[] a;
  
  public ArrayExample(T[] s){
    a = s;
  }

  public void display(){
    for (int i = 0; i < a.length; i++){
      System.out.print(a[i]+ " ");
    }
    System.out.println();
  }

  public int elementCount(T x){
    int count = 0;

    for (int i = 0; i < a.length; i++){
        if ( x instanceof Integer ){
            if (a[i] == x){
                count++;
            }
        }

        if ( x instanceof String){
            if ( a[i].equals(x)){
                count++;
            }
        }    }
    return count;
  }

}  
public class ArrayObject {
    public static void main(String[] args) {
        @SuppressWarnings("resource")
        Scanner sc = new Scanner(System.in);
        int len = sc.nextInt(); //int arr

        Integer[] x = new Integer[len];
        for ( int i = 0; i < len; i++){
            x[i] = sc.nextInt(); //int arr element
        }

        ArrayExample <Integer> obj = new ArrayExample<Integer>(x);
        
        int s1 = sc.nextInt(); // value to be counted

        String[] y = new String[len];
        for ( int i = 0; i < len; i++){
            y[i] = sc.next(); //String arr element
        }

        ArrayExample <String> obj1 = new ArrayExample<String>(y);
        String s2 = sc.next(); //Taking input for the value to be counted
        obj.display();
        System.out.println(obj.elementCount(s1));
        obj1.display();
        System.out.println(obj1.elementCount(s2));
      }
}
