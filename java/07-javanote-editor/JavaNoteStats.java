import java.util.*;
public class JavaNoteStats {
    public static void analyze(String content) {
        int words = content.trim().isEmpty() ? 0 : content.trim().split("\\s+").length;
        int lines = content.split("\R", -1).length;
        System.out.printf("Lines: %d | Words: %d | Chars: %d%n", lines, words, content.length());
    }
    public static void main(String[] args) {
        analyze("RiseAhead JavaNote\nClean modular text utility.");
    }
}
