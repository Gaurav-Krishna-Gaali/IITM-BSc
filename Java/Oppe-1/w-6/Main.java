import java.util.*;
class CricketPlayer{
  private String name;
  private int wickets;
  private int runs;
  private int matches;
  public CricketPlayer(String s, int w, int r, int m){
    this.name = s;
    this.wickets = w;
    this.runs = r;
    this.matches = m;
  }
  public String getName(){
    return name;
  }
  public int getWickets(){
    return wickets;
  }
  public int getRuns(){
    return runs;
  }
  public double avgRuns(){
    return runs/matches;
  }
  public double avgWickets(){
    return wickets/matches;
  }
} 
public class Main {

    public static void displayPlayers(ArrayList<CricketPlayer> bw, ArrayList<CricketPlayer> bt){
        for(int i=0; i<bw.size(); i++){
            System.out.print(bw.get(i).getName()+" ");
        }
        System.out.println("");
        for(int i=0; i<bt.size(); i++){
            System.out.print(bt.get(i).getName()+" ");
        }
    }

    public static void main(String[] args) {
        @SuppressWarnings("resource")
        Scanner sc = new Scanner(System.in);
        CricketPlayer p1 = new CricketPlayer(sc.next() ,sc.nextInt(), sc.nextInt(), sc.nextInt() );
        CricketPlayer p2 = new CricketPlayer(sc.next() ,sc.nextInt(), sc.nextInt(), sc.nextInt() );
        CricketPlayer p3 = new CricketPlayer(sc.next() ,sc.nextInt(), sc.nextInt(), sc.nextInt() );
        CricketPlayer p4 = new CricketPlayer(sc.next() ,sc.nextInt(), sc.nextInt(), sc.nextInt() );
        
        ArrayList <CricketPlayer> bt = new ArrayList<CricketPlayer>();
        ArrayList <CricketPlayer> bw = new ArrayList<CricketPlayer>();

        CricketPlayer[] all = {p1, p2, p3, p4};
        
        for (int i = 0; i < all.length; i++){
            if(all[i].avgRuns() > 25){
                bt.add(all[i]);
            }
            if(all[i].avgWickets() > 1){
                bw.add(all[i]);
            }
            }
    displayPlayers(bw, bt);
}  
}