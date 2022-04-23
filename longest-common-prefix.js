var longestCommonPrefix = function(strs) {
    strs.sort();
    var result = strs[0];
    var arrayLength = strs.length;
    for(var i = 1; i < arrayLength; i++) {
        for(var j = 0; j < strs[i].length; j++){
          if(result[j] == strs[i][j]){
            continue;
          }
          else{
            result = result.substring(0,j);
            break;
          }
        }
    }
    return result;
};