/*
 *Sentence Similarity
Determine if two sentences are similar. Two sentences are similar if they have the same length and each pair of corresponding words in the two sentences is similar. The similarity between words is defined by the provided list of similar word pairs. A word is always similar to itself.

For example, if we have the list of similar word pairs as [("great", "good"), ("acting","drama"), ("skills","talent")], then the sentences "You have great acting skills" and "You have good drama talent" are similar.


 */

package Pramp;
import java.util.*;

public class SentenceSimiliarity {
    static Map<String, List<String>> adjMap;
    public static boolean areSentencesSimilar(String[] sentence1, String[] sentence2, String[][] similarPairs) {
        // your code goes here
        adjMap = new HashMap<>();
        for(String[] pair: similarPairs) {
            adjMap.putIfAbsent(pair[0], new ArrayList<>());
            adjMap.putIfAbsent(pair[1], new ArrayList<>());
            adjMap.get(pair[0]).add(pair[1]);
            adjMap.get(pair[1]).add(pair[0]);
        }

        if(sentence1.length!=sentence2.length) return false;

        for(int i = 0; i<sentence1.length; i++) {
            if(!sentence1[i].equals(sentence2[i])) {
                if(!dfs(sentence1[i], sentence2[i], new HashSet<>())) return false;
            }
        }
        return true;
    }

    public static boolean dfs(String word1, String word2, HashSet<String> visited) {
        if(visited.contains(word1)) return false;
        if(!adjMap.containsKey(word1)) return false;
        if(word1.equals(word2)) return true;
        visited.add(word1);
        for(String neighbor: adjMap.get(word1)) {
            if(dfs(neighbor, word2, visited)) return true;
        }
        return false;
    }


    public static void main(String[] args) {
        String[] sentence1 = {"i", "really", "love", "leetcode", "and", "apples"};
        String[] sentence2 = {"i", "so", "like", "codesignal", "and", "oranges"};
        String[][] similarPairs = {
            {"very", "so"},
            {"love", "adore"},
            {"really", "very"},
            {"leetcode", "codesignal"},
            {"apples", "oranges"},
            {"like", "adore"},
        };

        boolean result = areSentencesSimilar(sentence1, sentence2, similarPairs);
        System.out.println(result); // Expected output: true
    }
}