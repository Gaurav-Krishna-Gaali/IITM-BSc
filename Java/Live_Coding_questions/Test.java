package Java.Live_Coding_questions;

import java.util.*;
//Add your code for Class Student here
class Student{
    private String name;
    private double marks[];
    public Student(String name , double[] marks){
        this.name = name;
        this.marks = marks;
    } 

    public String getName(){
        return name;
    }

    public double findTotal(){
        double total = 0.0;
        for ( double i : this.marks ){
            total += i;
        }
        return total;
    }
} 
public class Test{
    // Define the method getMax() here
    public static String getMax(Student[] students){
        double max = 0.0;
        String max_student = "";
        for (Student i : students){ 
           double total_marks = i.findTotal();
            if (total_marks > max){
                max = i.findTotal();
                max_student = i.getName();
            }
        }
        return max_student;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Student[] arr = new Student[3];   
        for(int i = 0; i < 3; i++){
            String name = sc.next();
            double[] m = {sc.nextDouble(), sc.nextDouble(), sc.nextDouble()};
            arr[i] = new Student(name, m);
        }
        System.out.println(getMax(arr));  
    }
}