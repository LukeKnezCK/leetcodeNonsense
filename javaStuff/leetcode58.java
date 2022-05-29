//Simple iterative soultion
class Solution {
    public int lengthOfLastWord(String s) {
        int counter = 0;
        int result = 0;
        for(int i = 0; i < s.length(); i++){
            if(s.charAt(i) != ' ') counter++;
            else if(counter > 0){
                result = counter;
                counter = 0;
            }
        }
        if(counter > 0) result = counter;
        return result;
    }
}

//regex version, java regex is pretty similar to python from what i can tell :p
import java.util.regex.Matcher;
import java.util.regex.Pattern;
class Solution {
    public int lengthOfLastWord(String s) {
        Pattern p = Pattern.compile("[a-zA-Z]*\s*$");
        Matcher m = p.matcher(s);
        m.find();
        return m.group(0).replaceAll("\\s","").length();
    }
}
