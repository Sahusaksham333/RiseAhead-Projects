import java.util.*;
public class SmartParking {
    private final PriorityQueue<Integer> freeSlots = new PriorityQueue<>();
    public SmartParking(int capacity) { for (int i = 1; i <= capacity; i++) freeSlots.offer(i); }
    public int park() { return freeSlots.isEmpty() ? -1 : freeSlots.poll(); }
    public void leave(int slot) { freeSlots.offer(slot); }
    public static void main(String[] args) {
        SmartParking sp = new SmartParking(5);
        int s1 = sp.park(), s2 = sp.park();
        sp.leave(s1);
        System.out.println("Next allocated nearest slot: " + sp.park());
    }
}
