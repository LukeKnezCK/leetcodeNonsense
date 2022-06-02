class Solution {
    public int maxDiff(int num) {
        String stringNum = Integer.toString(num);
        
        //Getting converted number 'a'
        char x = '0';
        int y = 9;
        for(int i = 0; i < stringNum.length(); i++){
            if(stringNum.charAt(i) == '9' && i == stringNum.length()-1){
                x = '9';
                break;
            }
            else if(stringNum.charAt(i) == '9') continue;
            else{
                x = stringNum.charAt(i);
                break;
            }
        }
        int a = 0;
        for(int j = 0; j < stringNum.length(); j++){
            if(stringNum.charAt(j) == x){
                a += y*Math.pow(10,stringNum.length()-j-1);
            }
            else{
                a += Character.getNumericValue(stringNum.charAt(j))*Math.pow(10,stringNum.length()-j-1);
            }
        }
        System.out.println(a);
        
        //Getting converted number 'b'
        y=1;
        for(int i = 0; i < stringNum.length(); i++){
            if(i == 0){
                if(Character.getNumericValue(stringNum.charAt(i)) > 1){
                    x = stringNum.charAt(i);
                    y = 1;
                    break;
                }
                else continue;
            }
            else{
                if(i == stringNum.length()-1){
                    if(stringNum.charAt(i) == '0' || stringNum.charAt(i) == stringNum.charAt(0)){
                        x = stringNum.charAt(0);
                        y = 1;
                        break;
                    }
                    else{
                        x = stringNum.charAt(i);
                        y = 1;
                        break;
                    }
                }
                else{
                    if(i > 0 && stringNum.charAt(i) == stringNum.charAt(0)) continue;
                    if(stringNum.charAt(i) == '0') continue;
                    else{
                        x = stringNum.charAt(i);
                        y = 0;
                        break;
                    }
                }
            }
        }
        int b = 0;
        for(int j = 0; j < stringNum.length(); j++){
            if(stringNum.charAt(j) == x){
                b += y*Math.pow(10,stringNum.length()-j-1);
            }
            else{
                b += Character.getNumericValue(stringNum.charAt(j))*Math.pow(10,stringNum.length()-j-1);
            }
        }
        System.out.println(b);
        
        return a-b;
    }
}