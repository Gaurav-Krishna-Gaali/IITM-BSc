import java.util.*;

class ComplexNum <T extends Number>{
    public Number real;
    public Number imag;

    public ComplexNum (Number real, Number imag) {
        this.real = real;
        this.imag = imag;
    }

    public <T extends Number> ComplexNum <T> add(ComplexNum <T> c){
        return new ComplexNum <>(this.real.doubleValue() + c.real.doubleValue(), this.imag.doubleValue() + c.imag.doubleValue());
    }
}

class Fclass1{
    public static void main(String[] args) {
            Scanner sc = new Scanner(System.in);
            int n1, n2;
            double d1, d2;
            n1 = sc.nextInt();
            n2 = sc.nextInt();
            d1 = sc.nextDouble();
            d2 = sc.nextDouble();
            ComplexNum<Integer> c1 = new ComplexNum<Integer>(n1, n2);
            ComplexNum<Double> c2 = new ComplexNum<Double>(d1, d2);
            ComplexNum<Double> c3 = c1.add(c2);
            System.out.println(c1 + " + " + c2 + " = " + c3);
        }
    }