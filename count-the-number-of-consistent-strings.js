var countConsistentStrings = function(allowed, words) {
    let count = 0;
    let found = false;
    for(let i=0; i<words.length; i++){
        found = false;
        for(let j=0; j<words[i].length; j++){
            if(allowed.includes(words[i][j])){
                found = true;
            }
            else{
            	found = false;
            }
            if(found === false){
                break;
            }
        }
        if(found){
            count++;
        }        
    }
  
    return count;
};
