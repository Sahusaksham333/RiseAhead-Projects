import java.util.*;
public class HotelBooking {
    private final Set<Integer> occupied = new HashSet<>();
    public boolean checkIn(int room) { return occupied.add(room); }
    public double checkOut(int room, int nights, double rate) {
        if (!occupied.remove(room)) return 0.0;
        return nights * rate * 1.12; // includes 12% GST
    }
    public static void main(String[] args) {
        HotelBooking hb = new HotelBooking();
        hb.checkIn(204);
        System.out.printf("Invoice Total: %.2f%n", hb.checkOut(204, 3, 2500.0));
    }
}
