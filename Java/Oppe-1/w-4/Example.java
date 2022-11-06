import java.util.*;


abstract class StringOperations{
  public abstract String reverse(String s);
  public abstract int vowelCount(String s);
}

abstract class StringReverse extends StringOperations{
    public String reverse(String s){
        String reverse = "";
        for (int i = s.length() - 1; i >= 0; i--){
            reverse += s.charAt(i);
        }
        return reverse;
    }

}


 class UpdatedStrings extends StringReverse{
    public int vowelCount(String s){
        int count = 0;
        char[] arr = {'a','e','i','o','u'};
        for (int i = 0; i < s.length();i++){
            for (int j = 0; j < arr.length; j++){
                if ( s.charAt(i) == arr[j]){
                    count ++;
                }
            }
        }
        return count;
    }
}


class Example {
    public static void main(String[] args) {
      Scanner sc = new Scanner(System.in);
      String s = sc.next();
      UpdatedStrings str = new UpdatedStrings();
      System.out.println("Reverse of "+ s + " is "+ str.reverse(s));
      System.out.println("Vowel count of "+ s + " is "+ str.vowelCount(s));
    }
  }