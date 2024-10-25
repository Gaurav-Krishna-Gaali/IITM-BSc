import java.util.*;
class Shape{
    public int area() {
        return 0;
    }
    public int volume() {
        return 0;
    }
}

class Rectangle extends Shape{
    private int w, h;

    public Rectangle(int w, int h){
        this.w = w;
        this.h = h;
    }

    public int area(){
        return w*h;
    }

}

class Cube extends Shape{
    private int a;
    
    public void Cube(int a){
        this.a = a;
    }

    public int volume(){
        return (a*a*a);
    }
}



public class Fclass2{
    private static void caller(Shape s){
        if (s instanceof Rectangle){
            System.out.println(s.area());
        }

        if (s instanceof Cube){
            System.out.println(s.volume());
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int w = sc.nextInt();
        int h = sc.nextInt();
        int a = sc.nextInt();
        caller(new Rectangle(w, h));
        caller(new Cube(a));
    }
}
