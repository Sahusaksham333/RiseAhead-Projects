import java.util.*;
public class BusReservation {
    private final boolean[] seats = new boolean[40];
    public boolean reserveSeat(int num) {
        if (num < 1 || num > 40 || seats[num - 1]) return false;
        seats[num - 1] = true;
        return true;
    }
    public static void main(String[] args) {
        BusReservation bus = new BusReservation();
        System.out.println("Seat 12 booked: " + bus.reserveSeat(12));
        System.out.println("Seat 12 again: " + bus.reserveSeat(12));
    }
}
