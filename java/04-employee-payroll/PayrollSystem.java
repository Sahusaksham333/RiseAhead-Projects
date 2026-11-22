import java.util.*;
public class PayrollSystem {
    record Employee(int id, String name, double baseSalary) {
        double netMonthly() { return (baseSalary * 1.20) - (baseSalary * 0.12); }
    }
    public static void main(String[] args) {
        List<Employee> staff = List.of(new Employee(1, "Priya", 80000), new Employee(2, "Rohan", 65000));
        for (Employee e : staff) System.out.printf("%s -> Net Monthly: %.2f%n", e.name(), e.netMonthly());
    }
}
