var restoreString = function(s, indices) {
    let sortedIndices = [...indices];
    sortedIndices.sort(function(a, b) {
  		return a - b;
		});
    let newSort = '';
    for(i=0; i<sortedIndices.length; i++){
    		console.log(sortedIndices[i]);
    		let index = indices.indexOf(sortedIndices[i]);
        newSort = s[index] + newSort;  
    }
  
    return newSort.split("").reverse().join("");
};
