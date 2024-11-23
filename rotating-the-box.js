var rotateTheBox = function(box) {
    let rows = box.length;
    let cols = box[0].length;

    for(row = 0; row < rows; row++){
        i = cols - 1;
        for(col = cols; col>=0; col-- ){
            if(box[row][col] == '#'){
                let temp = box[row][col];
                box[row][col] = box[row][i];
                box[row][i] = temp;
                i = i -1;
            }
            if(box[row][col] == '*'){
                i = col-1;
            }
        }
    }

    const rotated = [];

    for (let j = 0; j < cols; j++) {
        rotated[j] = [];
        for (let i = 0; i < rows; i++) {
            rotated[j][rows - 1 - i] = box[i][j];
        }
    }

    return rotated;
};
