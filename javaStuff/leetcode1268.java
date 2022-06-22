class Solution {
    public List<List<String>> suggestedProducts(String[] products, String searchWord) {
        Arrays.sort(products, String.CASE_INSENSITIVE_ORDER);
        String letters = "" + searchWord.charAt(0);
        int counter = 0;
        List<List<String>> results = new ArrayList<>();
        while(letters.length() <= searchWord.length()){
            List<String> layer = new ArrayList<>();
            for(String product : products){
                if(product.length() < letters.length()) continue;
                if(product.substring(0,counter+1).equals(letters)){
                    layer.add(product);
                    if(layer.size() == 3) break;
                }
            }
            results.add(layer);
            counter++;
            if(counter == searchWord.length()) break;
            letters = letters + searchWord.charAt(counter);
        }
        return results;
    }
}
