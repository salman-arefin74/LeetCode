
var digitSum = function(s, k) {
  while(s.length > k){
    let divide = s.match(new RegExp('.{1,' + k + '}', 'g'));
    
    let summedArray = [];
    let sum = 0;
    for(var i=0; i<divide.length; i++){
      sum = 0;
      for (var j = 0; j < divide[i].length; j++) {
            sum += parseInt(divide[i][j]);
        }
      summedArray.push(sum);
    }
    
    let concat = "";
    for (var i = 0; i < summedArray.length; i++) {
          concat += summedArray[i].toString();
      }
    s = concat;
  }
  return s;
};