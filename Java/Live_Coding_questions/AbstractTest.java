package Java.Live_Coding_questions;
import java.util.*;

abstract class UPIPayment{
    abstract void payment();
    abstract void rewards();
}
class PhonePay extends UPIPayment{
    private int amount;
    public PhonePay(int amount) {
        this.amount = amount;
    } 
    // Oveeride method payment()
    public void payment() {
        System.out.println("Phone pay:Payment success:");
        rewards();
    }
    // Override method rewards()
    public void rewards(){
        if( amount < 500){
            System.out.println("Sorry no rewards");
        } else if( amount >= 500){
            System.out.println("10 off on next mobile rc");
        }
    }
}
class Paytm extends UPIPayment{
    private int amount;
    public Paytm(int amount) {
        this.amount = amount;
    }
    // Oveeride method payment()
    public void payment() {
        System.out.println("Paytm:Payment success:");
        rewards();
    }
    // Override method rewards()
    public void rewards(){
        if( amount < 500){
            System.out.println("Sorry no rewards");
        } else if( amount >= 500){
            System.out.println("10 off on next DTH rc");
        }
    }
}
class UPIUser{
    public void transferAndGetRewards(UPIPayment obj) {
        obj.payment();
    }
}
public class AbstractTest {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a1 = sc.nextInt();
        int a2 = sc.nextInt();
        UPIUser u = new UPIUser(); 
        u.transferAndGetRewards(new PhonePay(a1));
        u.transferAndGetRewards(new Paytm(a2));
   }
}