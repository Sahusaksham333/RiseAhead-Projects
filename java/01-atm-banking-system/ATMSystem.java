import java.util.*;
public class ATMSystem {
    private final Map<String, Double> balances = new HashMap<>();
    public ATMSystem() { balances.put("1001", 15000.0); balances.put("1002", 8500.0); }
    public boolean transfer(String src, String dst, double amt) {
        if (amt <= 0 || balances.getOrDefault(src, 0.0) < amt || !balances.containsKey(dst)) return false;
        balances.put(src, balances.get(src) - amt);
        balances.put(dst, balances.get(dst) + amt);
        return true;
    }
    public static void main(String[] args) {
        ATMSystem atm = new ATMSystem();
        System.out.println("Transfer 2500: " + atm.transfer("1001", "1002", 2500));
        System.out.println("Balances: " + atm.balances);
    }
}
