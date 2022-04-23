var truncateSentence = function(s, k) {
    let newArr = s.split(' ');
    let trunc = newArr[0];
    for(let i=1; i<k; i++){
        trunc = trunc + ' ' + newArr[i];
    }
  
    return trunc;
};