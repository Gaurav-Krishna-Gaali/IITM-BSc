import java.util.*;

public class Test2{
    public static boolean balanceCheck(String sequence) {
        Stack <Character> balancer = new Stack<Character>();

        for (int i = 0; i < sequence.length(); i++) {
            Character curr_char = sequence.charAt(i);
            if(curr_char != '(' && curr_char != '{' && curr_char != '[' && 
                curr_char != ')'&& curr_char != '}' && curr_char != ']') {
				                continue;
			            }

            if(curr_char == '(' || curr_char == '{' || curr_char == '[') {
                balancer.push(curr_char);
            }

            if(balancer.isEmpty()) 
                return false;
            else if(curr_char == ')'){
                if (balancer.peek() != '('){ //
                    return false;
                } else{
                    balancer.pop();
                }
            } 
            else if(curr_char == '}'){
                if (balancer.peek() != '{'){ //
                    return false;
                } else{
                    balancer.pop();
                }
            } 
            else if(curr_char == ']'){
                if (balancer.peek() != '['){ //
                    return false;
                } else{
                    balancer.pop();
                }
            } 
            
        }
        return balancer.isEmpty();

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