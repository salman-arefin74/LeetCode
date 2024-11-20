var removeElement = function (nums, val) {
    let arrLength = nums.length;
    for (let i = 0; i < arrLength; i++) {
        if (nums[i] === val) {
            nums.splice(i, 1);
            i--;
            arrLength--;
        }
    }
};
