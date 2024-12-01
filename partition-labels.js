var partitionLabels = function(s) {
    let hashMap = {};
    let result = [];
    for(let i = 0; i < s.length; i++){
        hashMap[s[i]] = i;
    }
    
    let max = 0;
    let prev = -1;
    for(let i = 0; i < s.length; i++){
        let letter = s[i];
        let lastIndex = hashMap[letter];
        max = Math.max(max, lastIndex);
        if(max == i){
            result.push(max - prev);
            prev = max;
        }
    }

    return result;
};

