var checkIfPangram = function(sentence) {
    if(sentence.length < 26){
        return false;
    }   
    else{
        let alphabet = 'a';
        let found = false;
        for(let i=0; i<26; i++){
            alphabet = String.fromCharCode(97 + i);
            if(sentence.includes(alphabet)){
                found = true;
            }
            else{
                found = false;
            }
            if(!found){
                break;
            }
        }
        if(found){
            return true;
        }
        else{
            return false
        }
    }
};