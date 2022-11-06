import java.util.*;

interface Iterator{
    public boolean has_next();
    public Object get_next();
}

class Sequence{
    private final int maxLimit = 80;
    private SeqIterator _iter = null;
    int[] iArr; 
    int size;
    static int ind = 0;

    public Sequence(int maxLimit){
        this.size = maxLimit;
        iArr = new int[size];
    }

    public void addTo(int a){
        if (ind < size){
            iArr[ind] = a;
            ind++;
        }
    }

    public Iterator get_Iterator(){
        _iter = new SeqIterator();
        return (_iter);
    }

    private class SeqIterator implements Iterator{
        int indx = 0;
        public SeqIterator(){
            indx = -1;
        }

        public boolean has_next(){
            if (indx < size-1){
                return true;
            } else {
                return false;
            }
        }

        public Object get_next(){
            if (has_next()){
                indx ++;
            }
            return (iArr[indx]);
        }
    }

}

public class Fclassgrpa {
    public static void main(String[] args) {
        Sequence sObj = new Sequence(5);
        Scanner sc = new Scanner(System.in); 
        for(int i = 0; i < 5; i++) {
            sObj.addTo(sc.nextInt());
        }
        Iterator i = sObj.get_Iterator();
        while(i.has_next())
            System.out.print(i.get_next() + ", ");
    }
    
}
