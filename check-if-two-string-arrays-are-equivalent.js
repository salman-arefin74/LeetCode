var arrayStringsAreEqual = function(word1, word2) {
    let sentence1 = '';
    let sentence2 = '';
    for(let i=0; i<word1.length; i++){
        sentence1 = sentence1 + word1[i];
    }
    for(let i=0; i<word2.length; i++){
        sentence2 = sentence2 + word2[i];
    }
    if(sentence1 == sentence2){
        return true;
    }
    else{
        return false;
    }
};