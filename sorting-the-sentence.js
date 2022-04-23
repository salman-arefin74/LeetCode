var sortSentence = function(s) {
    let words = s.split(' ');
    let sentence = '';
    for(let i=0; i<words.length; i++){
        words[i] = words[i].split("").reverse().join("");
    }
    words.sort();
    for(let i=0; i<words.length; i++){
        words[i] = words[i].split("").reverse().join("");
        words[i] = words[i].slice(0,-1);
    }
    sentence = words[0];
    for(let i=1; i<words.length; i++){
        sentence = sentence + ' ' + words[i];
    }
    return sentence;
};