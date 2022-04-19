
var largestInteger = function(num) {
  let str = num.toString();
  
  let even = [];
  let odd = [];
  for(var i = 0; i<str.length; i++){
    if(parseInt(str[i])%2 == 0){
      even.push(parseInt(str[i]));
    }
    else{
      odd.push(parseInt(str[i]));
    }
  }
  even.sort(function(a, b){return b-a});
  odd.sort(function(a, b){return b-a});
  
  let newArr = "";
  let oddIndex = 0;
  let evenIndex = 0;
  for(var i = 0; i<str.length; i++){
    if(parseInt(str[i])%2 != 0){
      newArr = newArr + odd[oddIndex];
      oddIndex++;
    }
    else{
      newArr = newArr + even[evenIndex];
      evenIndex++;
    }
  }
  
  return parseInt(newArr);  
};