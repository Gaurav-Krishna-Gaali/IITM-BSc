import java.util.*;
class Person{
    private String name;
    private long aadharno;
    public Person(String name, long aadharno){
        this.name = name;
        this.aadharno = aadharno;
    }
    public void print() {
        System.out.println("name : " + name);
        System.out.println("aadharno : " + aadharno);
    }
}

class Employee extends Person{
    private double salary;
public Employee(String n, long a, Double s){
    super (n,a);
    salary=s;
//         this.name=nm1;
//         this.aadharno=adh1;
//         this.salary=sal;
}

//     //override print method
public void print(){
super.print();
//         System.out.println("name : "+this.name);
//         System.out.println("aadharno : "+this.aadharno);
System.out.println("salary : "+salary);
}
}

class ContactEmployee extends Employee{
final private static double hourlyPay = 100.00;
private int contactHour;

//     //implement the constructor
public ContactEmployee(String na, long aa, int c){
super(na,aa,(double)c* hourlyPay);
//         this.name=nm2;
//         this.aadharno=adh2;
//         this.contactHour=cont;
}
//     //salary is computed as contactHour * hourlyPay  
public void print(){
super.print();
//         public double sal= contactHour * hourlyPay;
//         System.out.println("name : "+this.name);
//         System.out.println("aadharno : "+this.aadharno);
//         System.out.println("salary : "+this.sal);
}

}

class FClass{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String nm1 = sc.nextLine();
        String nm2 = sc.nextLine();
        long adh1 = sc.nextLong();
        long adh2 = sc.nextLong();
        double sal = sc.nextDouble();
        int cont = sc.nextInt();
        Employee[] eArr = new Employee[2];
        eArr[0] = new Employee(nm1, adh1, sal);
        eArr[1] = new ContactEmployee(nm2, adh2, cont);
        for(Employee e : eArr)
            e.print();
    }
}