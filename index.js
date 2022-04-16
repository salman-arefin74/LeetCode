var myStringArray = ["flower","flow", "flaod"];
myStringArray.sort();
var result = myStringArray[0];
var arrayLength = myStringArray.length;
for(var i = 1; i < arrayLength; i++) {
    for(var j = 0; j < myStringArray[i].length; j++){
      if(result[j] == myStringArray[i][j]){
        continue;
      }
      else{
        result = result.substring(0,j);
        break;
      }
    }
}

console.log(result);