var lengthOfLastWord = function(s) {
    let newString = s.replace(/\s+/g,' ');
    let urlParts = newString.split(' ');
    if(urlParts[urlParts.length-1] === '')
    	return urlParts[urlParts.length-2].length;
    else
    	return urlParts[urlParts.length-1].length;
};