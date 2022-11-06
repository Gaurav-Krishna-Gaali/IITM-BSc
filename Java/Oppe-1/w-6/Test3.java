import java.util.*;

public class Test3{
    public static boolean balanceCheck(String sequence) {
        // usse stack to check the balabce

        Stack<Character> brackets = new Stack<Character>();
        char[] left = {'{','(','['};
        char[] right = {'}',')',']'};

        HashMap<Character, Character> map = new HashMap<>();

        map.put('(' , ')');
        map.put('{' , '}');
        map.put('[' , ']');

        for (int i = 0 ; i < sequence.length(); i++){
            char x = sequence.charAt(i);

            boolean leftContains = false;
            boolean rightContains = false;

            for(int j = 0; j < left.length; j++){
                if (left[j] == x){
                    leftContains = true;
                }
            }

            for ( int j = 0; j < right.length; j++){
                if (right[j] == x){
                    rightContains = true;
                }
            }

            if (leftContains){
                brackets.add(x);
            } else if (rightContains){
                if(brackets.isEmpty()){
                    return false;
                }
                char y = brackets.pop();
                if (map.get(y) != x){
                    return false;
                }
            }
        }

        if(brackets.isEmpty()){
            return true;
        }
        return false;
    }
   
    public static void main(String args[]) {
        @SuppressWarnings("resource")
        Scanner s = new Scanner(System.in);
        
        ArrayList<String> expr_arr= new ArrayList<String>();
        String inp=null;
        
        do {
            inp = s.nextLine();
            if(!inp.equalsIgnoreCase("Done"))
                expr_arr.add(inp);
        }while(!inp.equalsIgnoreCase("Done"));

        for(String expr : expr_arr) {
            if(balanceCheck(expr)) {
                System.out.println("Balanced");
            }
            else {
                System.out.println("Not Balanced");
            }
        }
    }
}     