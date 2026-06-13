class Solution {

    public String mapWordWeights(String[] words, int[] weights) {

        StringBuilder answer = new StringBuilder();

        for(String word : words) {

            int sum = 0;

            for(char ch : word.toCharArray()) {
                sum += weights[ch - 'a'];
            }

            int mod = sum % 26;

            answer.append((char)('z' - mod));
        }

        return answer.toString();
    }
}
