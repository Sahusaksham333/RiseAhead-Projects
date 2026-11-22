import java.util.*;
public class AirlineReservation {
    private final Map<String, Integer> seats = new HashMap<>();
    public AirlineReservation() { seats.put("AI-202", 3); seats.put("6E-509", 5); }
    public String book(String flight, String passenger) {
        int avail = seats.getOrDefault(flight, 0);
        if (avail <= 0) return "WAITLISTED";
        seats.put(flight, avail - 1);
        return "PNR-" + flight + "-" + Math.abs(passenger.hashCode() % 10000);
    }
    public static void main(String[] args) {
        AirlineReservation ar = new AirlineReservation();
        System.out.println("Booked: " + ar.book("AI-202", "Aarav"));
    }
}
