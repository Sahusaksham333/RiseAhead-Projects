import java.util.*;
public class InventoryManager {
    private final Map<String, Integer> stock = new HashMap<>();
    public void addStock(String sku, int qty) { stock.merge(sku, qty, Integer::sum); }
    public List<String> lowStockAlerts(int threshold) {
        List<String> alerts = new ArrayList<>();
        stock.forEach((k, v) -> { if (v < threshold) alerts.add(k + " (" + v + ")"); });
        return alerts;
    }
    public static void main(String[] args) {
        InventoryManager im = new InventoryManager();
        im.addStock("SKU-101", 4); im.addStock("SKU-102", 25);
        System.out.println("Low stock alerts: " + im.lowStockAlerts(10));
    }
}
