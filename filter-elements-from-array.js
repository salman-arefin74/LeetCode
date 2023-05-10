var filter = function(arr, fn) {
    var newArray = [];
    for(let i=0; i<arr.length; i++){
        if(fn(arr[i], i)){
            newArray.push(arr[i]);
        }
    }
    return newArray;
};
