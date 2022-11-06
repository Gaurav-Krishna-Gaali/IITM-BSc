import java.util.*;

class Employee{
    String eid;
    String ename;
    String eprojects[];

    public  Employee(String ename, String eid, String[] eprojects){
        this.ename = ename;
        this.eid = eid;
        this.eprojects = eprojects;
        
    }

    public Employee(Employee e){
        this.ename = e.ename;
        this.eid = e.eid;
        this.eprojects = new String[e.eprojects.length];
        for(int i = 0;  i < e.eprojects.length; i++){
            this.eprojects[i] = e.eprojects[i];
        }
    }

    public void display(){
        System.out.println("id: "+this.ename);
        System.out.println("name: "+this.eid);
        System.out.println("projects:");
        for ( String s : eprojects){
            System.out.print(s+":");
        }
        System.out.print("\n");
    }



public void mutator(){
    this.ename = "Mr "+this.ename;
    this.eprojects[0] = null;
}

}
public class FClass1{
    public static void main(String[] args) 
    {
        try (Scanner s = new Scanner(System.in)) {
            String project[] = {"P001","P002","P003"};
            //Enter the id of employee
            String id = s.nextLine();
            //Enter the name of employee
            String name = s.nextLine();
            
            Employee e1 = new Employee(id,name,project);
            Employee e2 = new Employee(e1); 
            //The copy constructor must copy all the data members. 
      
            e1.mutator();
            
            e2.display();
        }
    }
}