import java.util.*;
public class VotingPortal {
    private final Set<String> voted = new HashSet<>();
    private final Map<String, Integer> tally = new HashMap<>();
    public boolean castVote(String voterId, String candidate) {
        if (!voted.add(voterId)) return false;
        tally.merge(candidate, 1, Integer::sum);
        return true;
    }
    public static void main(String[] args) {
        VotingPortal vp = new VotingPortal();
        vp.castVote("V1", "Alice"); vp.castVote("V2", "Bob"); vp.castVote("V1", "Bob");
        System.out.println("Results: " + vp.tally);
    }
}
