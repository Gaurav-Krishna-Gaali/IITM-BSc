import java.util.Scanner;

class Employee{
    String ename;
    String eid;
    String edept;

    public Employee(){
        ename = "guest";
    }

    public Employee(String ename, String eid, String edept){
        this.ename = ename;
        this.eid = eid;
        this.edept = edept;
    }

    public void copyDept(Employee e){
        this.edept = e.edept;
    }

    public void displayDetails(){
        System.out.println("ename:" + this.ename);
        System.out.println("eid:" + this.eid);
        System.out.println("edept:" + this.edept);
    }

}

public class FClass {
    public static void main(String args[]) 
	    {
		        try (Scanner s = new Scanner(System.in)) {
                    Employee e1 = new Employee();

                    //Enter name of the employee
                    String name = s.nextLine();

                    //Enter id of the employee
                    String id = s.nextLine();

                    //Enter department of the employee
                    String dept = s.nextLine();

                    Employee e2 = new Employee(name,id,dept);

                    e1.copyDept(e2); 
                    //Copies the department name of e2 into e1's department name.

                    e1.displayDetails();
                }
	    }
}

