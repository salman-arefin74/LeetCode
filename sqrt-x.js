var mySqrt = function(x) {
    let num = 0;
    let square = 0;
    while(square < x){
        num++;
        square = num * num;
        if(square > x) 
            num--;
    }
    return num;
};