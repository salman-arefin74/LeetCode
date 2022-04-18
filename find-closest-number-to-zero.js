var findClosestNumber = function(arr) {
  arr.sort(function(a, b){return a-b});
  
  let close = arr[arr.length - 1];
  let diff = arr[arr.length - 1];
  for(var i = arr.length - 1; i >= 0; i--){
    let newClose = 0;
    if(arr[i] < 0){
      newClose = arr[i] * (-1);
    }
    else{
      newClose = arr[i];
    }
  
    if(newClose < close){
        close = newClose;
        diff = arr[i];
    }
  }
  
  return diff;  
};