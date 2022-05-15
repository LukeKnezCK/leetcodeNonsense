

class Solution {
    public static int firstUniqChar(String s) {
        int counter [] = new int[26];
        for(int i = 0; i < s.length(); i++){
            counter[s.charAt(i) - 'a']++;
        }
        for(int i = 0; i < s.length(); i++){
            if(counter[s.charAt(i)-'a'] == 1){
                return i;
            }
        }
        return -1;
    }
}

//alt solution
class Solution {
    public int firstUniqChar(String s) {
        LinkedHashMap<Character, Integer> encounters = new LinkedHashMap<>();
        for(int i = 0; i < s.length(); i++){
            Character encounter = s.charAt(i);
            if(encounters.containsKey(encounter)) encounters.replace(encounter,-1);
            else encounters.put(encounter, i);
        }
        int result = -1;
        for(Map.Entry<Character, Integer> mapElement: encounters.entrySet()){
            if(mapElement.getValue()>-1){
                result = mapElement.getValue();
                return result;
            }
        }
        return result;
    }
}
