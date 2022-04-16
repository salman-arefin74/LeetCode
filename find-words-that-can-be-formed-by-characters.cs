public class Solution {
    public int CountCharacters(string[] words, string chars) {
        char[] dummy = "".ToCharArray();
		dummy = chars.ToCharArray();
        bool foundChar = false;
        int charNums = 0;
        for(int i = 0; i < words.Length; i++){
            for(int j = 0; j < words[i].Length; j++){
                foundChar = false;
                for(int k = 0; k < dummy.Length; k++){
                    if(words[i][j] == dummy[k]){
                        dummy[k] = '0';
                        foundChar = true;
                        break;
                    }
                }
                if(foundChar == false){
                    break;
                }
            }
            if(foundChar == true){
                charNums = charNums + words[i].Length;
            }
            dummy = chars.ToCharArray();
        }
        return charNums;
    }
}