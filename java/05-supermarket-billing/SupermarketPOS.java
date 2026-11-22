import java.util.*;
public class SupermarketPOS {
    public static void main(String[] args) {
        Map<String, Double> cart = Map.of("Rice 5kg", 380.0, "Olive Oil", 640.0, "Coffee", 290.0);
        double subtotal = cart.values().stream().mapToDouble(Double::doubleValue).sum();
        double gst = subtotal * 0.05;
        System.out.printf("Subtotal: %.2f | GST(5%%): %.2f | Grand Total: %.2f%n", subtotal, gst, subtotal + gst);
    }
}
